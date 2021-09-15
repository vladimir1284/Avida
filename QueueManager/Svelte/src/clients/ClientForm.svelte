<script>
    import { createForm } from "svelte-forms-lib";
    import { Button } from 'sveltestrap';
    import { Col, Row } from 'sveltestrap'
    import TrashCan from "svelte-material-icons/TrashCan.svelte";
    import { Form, FormGroup, Input, Label } from 'sveltestrap';
    import * as yup from 'yup';
	  import { base_url, clients } from '../stores.js';
    import { get } from 'svelte/store'

    export let openform
    export let client 
    let result
    let errors = {}

    const phoneRegExp = /(^$)|(^[0-9]{8}$)/

    const extractErrors = err => {
        return {[err.path]: err.message };
    };

    // Convert empty string into null
    function emptyStr2null(value, originalValue) { 
      if (!value) { 
        return null; 
      } 
      return originalValue; 
    }

    let schema = yup.object().shape({
      name: yup.string().required('Debes introducir un nombre'),
      cel: yup.string().matches(phoneRegExp, 'Este número celular no es válido').nullable(true).default(null).transform(( emptyStr2null)),
      phone: yup.string().matches(phoneRegExp, 'Este número fijo no es válido').nullable(true).default(null).transform(( emptyStr2null)),
      address: yup.string().required('Necesitamos la dirección'),
      fbid: yup.string().nullable(true).default(null).transform(( emptyStr2null)),
    });

    const { form, handleChange, handleSubmit } = createForm({
      initialValues: client,
      onSubmit: values => {
        result = schema.validate(values)
        result.then(
          () => {
            const castedValues = schema.cast(values)
            fetch(base_url+'new_client/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                  "X-CSRFToken": document.getElementsByTagName("input").csrfmiddlewaretoken.value,
                },
                body: JSON.stringify(castedValues),
              })
              .then(response => response.json())
              .then(values => {
                // Locally store the new client
                castedValues['id'] = values.id
                const clientes = get(clients)
                clientes[values.id] = castedValues
                clients.set(clientes)
              })
              .catch((error) => {
                console.error('Error:', error);
            });
            openform = false
          }
        ).catch(value => {
          errors = extractErrors(value)
          console.log(errors)
        });
      }
    });

    function delete_client(event){
      event.preventDefault(); // Avoids form close
      let confirmAction = confirm("¿Quieres borrar este cliente?");
      if (confirmAction) {
        const values = {'id':client.id};
        // values['csrfmiddlewaretoken'] = document.getElementsByTagName("input").csrfmiddlewaretoken.value;
        fetch(base_url+'del_client/', {
                method: 'POST', // or 'PUT'
                headers: {
                  'Content-Type': 'application/json',
                  "X-CSRFToken": document.getElementsByTagName("input").csrfmiddlewaretoken.value,
                },
                body: JSON.stringify(values),
              })
              .then(response => response.json())
              .then(values => {
                // Locally remove the client
                const clientes = get(clients)
                delete clientes[client.id];
                clients.set(clientes)
                openform = false;
              })
              .catch((error) => {
                console.error('Error:', error);
            });
        openform = false;
      }
    }
</script>

<Form on:submit={handleSubmit}>
  <FormGroup>
    <Label for="name">Nombre: *
      <small class="text-danger">{#if errors.name}{errors.name}{/if}</small></Label>
    <Row>
      <Col xs=11>
        <Input id="name"
        type="name"
        name="name"
        invalid={errors.name}
        on:change={handleChange}
        bind:value={$form.name}
        />
      </Col>
      <Col xs=1>
          <Button on:click={delete_client} color="danger"><TrashCan color="white"/></Button> 
      </Col>
    </Row>
  </FormGroup>
  <small class="text-danger">
    {#if errors.fbid}{errors.fbid}{/if}  
    {#if errors.phone}{errors.phone}{/if}
    {#if errors.cel}{errors.cel}{/if}
  </small>
  <Row>
    <Col xs="4">
      <FormGroup>
        <Label for="cel">Celular:</Label>
        <Input id="cel"
        type="number"
        name="cel"
        invalid={errors.cel}
        on:change={handleChange}
        bind:value={$form.cel}
        />
      </FormGroup>
    </Col>

    <Col xs="4">
      <FormGroup>
        <Label for="phone">Teléfono Fijo:</Label>
        <Input id="phone"
        type="number"
        name="phone"
        invalid={errors.phone}
        on:change={handleChange}
        bind:value={$form.phone}
        />
      </FormGroup>
    </Col>

    <Col xs="4">
      <FormGroup>
          <Label for="fbid">Facebook ID:</Label>
          <Input id="fbid"
          type="number"
          name="fbid"
          invalid={errors.number}
          on:change={handleChange}
          bind:value={$form.fbid}
          />        
      </FormGroup>
    </Col>
  </Row>

  <FormGroup>
    <Label for="address">Dirección: * 
      <small class="text-danger">{#if errors.address}{errors.address}{/if} </small></Label>
    <Input id="address"
    type="textarea"
    name="address"
    invalid={errors.address}
    on:change={handleChange}
    bind:value={$form.address}
    />     
  </FormGroup>


  <Row>
    <Col class="text-center" xs="6">
      <Button on:click={() => {openform = false;}} color='danger'>Cancelar</Button>
    </Col>
    <Col class="text-center" xs="6">
      <Button color='success' type="submit">Submit</Button>
    </Col>
  </Row>
</Form>

<style>
</style>
