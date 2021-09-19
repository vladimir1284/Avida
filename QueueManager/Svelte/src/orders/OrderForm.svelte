<script>
    import { createForm } from "svelte-forms-lib";
    import { Button } from 'sveltestrap';
    import { Col, Row } from 'sveltestrap'
    import {fetch_data} from '../utils'
    import { Form, FormGroup, Input, Label, InputGroupText, InputGroup } from 'sveltestrap';
    import {
      Dropdown,
      DropdownItem,
      DropdownMenu,
      DropdownToggle
    } from 'sveltestrap';
	  import { base_url, clients, orders } from '../stores.js';
    import * as yup from 'yup';
    import { get } from 'svelte/store'
    var { DateTime } = require('luxon');

    export let openform
    export let order 


    let result
    let errors = {}
    let selectedClient=""
    let clientes = Object.values(get(clients))
    let filteredClients = clientes
    let isOpen = false;

    $:{
        clientes = Object.values($clients)
    }

    const extractErrors = err => {
        return {[err.path]: err.message };
    };

    let schema = yup.object().shape({
      client: yup.number().required('Debes seleccionar un cliente'),
      lts: yup.number().min(15 ,"Deben ser más de 15L por pedido"),
      available: yup.date().nullable(true)
    });

    // Init form
    let initial_values = {
                            "client": null,
                            "lts": 20,
                            "available": null
                            };
    if (order !== null){
      initial_values = order
      initial_values.available = DateTime.fromISO(initial_values.available).setZone('local').toFormat("yyyy-MM-dd'T'HH:mm")
      selectedClient = get(clients)[initial_values.client].name
    }
    const { form, handleChange, handleSubmit } = createForm({
      initialValues: initial_values,
      onSubmit: values => {
        result = schema.validate(values)
        result.then(
          () => {
            if(values.available){
              values.available = DateTime.fromISO(values.available)
            }
            fetch(base_url+'new_order/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                  "X-CSRFToken": document.getElementsByTagName("input").csrfmiddlewaretoken.value,
                },
                body: JSON.stringify(values),
              })
              .then(response => response.json())
              .then(() => {
                // Get the orders from server again
                fetch_data('orders', 'get_orders/', orders)
              })
              .catch((error) => {
                console.error('Error:', error);
            });
            // alert(JSON.stringify(values))
            openform = false
          }
        ).catch(value => {
          errors = extractErrors(value)
          console.log(errors)
        });
      }
    });

    $:{searchClient(selectedClient)}

    function searchClient(input_str){
      filteredClients = []
      const filter = input_str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase();
      clientes.forEach((client) => {
        const txtValue = client.name.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          filteredClients.push(client)
        }
      })
    }

  function pickClient(event){ 
    selectedClient = event.target.innerHTML
    isOpen = true
    $form.client = parseInt(event.target.id)
  }

    function exit(){
      openform = false
    }
</script>


<Form on:submit={handleSubmit} autocomplete="off">
  <Row>
    <Col xs="12">      
      <small class="text-danger">{#if errors.client}{errors.client}{/if}</small>
      <FormGroup style="display: inline-flex;">
        <Label for="client_name">Cliente:* &nbsp;</Label>
        <Dropdown {isOpen} toggle={() => isOpen = !isOpen}>
          <DropdownToggle tag="div" class="d-inline-block">            
            <Input id="clientFilter"
            type="text"
            name="client_name"
            invalid={errors.client}
            bind:value={selectedClient}
            />
          </DropdownToggle>
          <DropdownMenu>
            {#each filteredClients as client, index}
              {#if index < 5}
                <DropdownItem on:click={pickClient} id={client.id}>{client.name}</DropdownItem>    
              {/if}          
            {/each}
            {#if filteredClients.length == 0}
              <DropdownItem disabled>Nadie con ese nombre...</DropdownItem>              
            {/if}
          </DropdownMenu>
        </Dropdown>
      </FormGroup>
    </Col>
  </Row>

  <Row>
    <Col xs="4">
      <FormGroup>
        <Label for="lts">Cantidad: * 
          <small class="text-danger">{#if errors.lts}{errors.lts}{/if} </small></Label>
        <InputGroup>
          <Input id="lts"
          type="number"
          name="lts"
          invalid={errors.lts}
          on:change={handleChange}
          bind:value={$form.lts}
          />     
          <InputGroupText id="litros">L</InputGroupText>
        </InputGroup>
      </FormGroup>
    </Col>
    <Col xs="8">     
      <Label for="lts">Disponible: * 
        <small class="text-danger">{#if errors.lts}{errors.lts}{/if} </small></Label>
      <InputGroup>
        <Input
        bind:value={$form.available}
        type="datetime-local"
        name="available"
        id="pickDatetime"
        />
    </InputGroup>
  </Col>
</Row>

  <Row>
    <Col class="text-center" xs="6">
      <Button on:click={exit} color='danger'>Cancelar</Button>
    </Col>
    <Col class="text-center" xs="6">
      <Button color='success' type="submit">Listo</Button>
    </Col>
  </Row>
</Form>

<style>
</style>
