<script>
    import { createForm } from "svelte-forms-lib";
    import { Button } from 'sveltestrap';
    import { Col, Row } from 'sveltestrap'
    import { Form, FormGroup, Input, Label, InputGroupText, InputGroup } from 'sveltestrap';
    import {
      Dropdown,
      DropdownItem,
      DropdownMenu,
      DropdownToggle
    } from 'sveltestrap';
    import {clientes} from '../backend'
    import * as yup from 'yup';

    export let openform
    export let order 
    let result
    let errors = {}
    let selectedClient=""
    let filteredClients = clientes
    let isOpen = false;

    const extractErrors = err => {
        return {[err.path]: err.message };
    };

    let schema = yup.object().shape({
      client_id: yup.number().required('Debes seleccionar un cliente').nullable(),
      lts: yup.number().min(20,"Deben ser más de 20L por pedido"),
      available: yup.date().nullable()
    });

    const { form, handleChange, handleSubmit } = createForm({
      initialValues: order,
      onSubmit: values => {
        result = schema.validate(values)
        result.then(
          () => {
            alert(JSON.stringify(values))
            openform = false
          }
        ).catch(value => {
          errors = extractErrors(value)
          console.log(errors)
        });
      }
    });

    function searchClient(){
      filteredClients = []
      const input = document.getElementById("clientFilter");
      const filter = input.value.toUpperCase();
      clientes.forEach((client) => {
        const txtValue = client.name.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          filteredClients.push(client)
        }
      })
    }

  function pickClient(event){ 
    selectedClient = event.target.innerHTML
    $form.client_id = parseInt(event.target.id)
    console.log(form)
  }

    function exit(){
      openform = false
    }
</script>


<Form on:submit={handleSubmit} autocomplete="off">
  <Row>
    <Col xs="12">      
      <small class="text-danger">{#if errors.client_id}{errors.client_id}{/if}</small>
      <FormGroup style="display: inline-flex;">
        <Label for="client_name">Cliente:* &nbsp;</Label>
        <Dropdown {isOpen} toggle={() => isOpen = !isOpen}>
          <DropdownToggle tag="div" class="d-inline-block">            
            <Input id="clientFilter"
            type="text"
            name="client_name"
            invalid={errors.client_id}
            on:keyup={searchClient}
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
      <Button color='success' type="submit">Crear</Button>
    </Col>
  </Row>
</Form>

<style>
</style>
