<script>
    import { createForm } from "svelte-forms-lib";
    import { Button } from 'sveltestrap';
    import { Col, Row } from 'sveltestrap'
    import { Form, FormGroup, Input, Label } from 'sveltestrap';
    import * as yup from 'yup';

    export let openform
    export let client 
    let result
    let errors = {}

    const phoneRegExp = /(^$)|(^[0-9]{8}$)/

    const extractErrors = err => {
        return {[err.path]: err.message };
    };

    let schema = yup.object().shape({
      name: yup.string().required('Debes introducir un nombre'),
      cel: yup.string().matches(phoneRegExp, 'Este número celular no es válido').nullable(),
      phone: yup.string().matches(phoneRegExp, 'Este número fijo no es válido').nullable(),
      address: yup.string().required('Necesitamos la dirección'),
      fbid: yup.string().nullable(),
      // createdOn: yup.date().default(function () {
      //   return new Date();
      // }),
    });

    const { form, handleChange, handleSubmit } = createForm({
      initialValues: client,
      onSubmit: values => {
        result = schema.validate(values)
        result.then(
          () => {
            alert(JSON.stringify(values))
            // openform = false
          }
        ).catch(value => {
          errors = extractErrors(value)
          console.log(errors)
        });
      }
    });
    function exit(){
      openform = false
    }
</script>

<Form on:submit={handleSubmit}>
  <FormGroup>
    <Label for="name">Nombre: *
      <small class="text-danger">{#if errors.name}{errors.name}{/if}</small></Label>
    <Input id="name"
    type="name"
    name="name"
    invalid={errors.name}
    on:change={handleChange}
    bind:value={$form.name}
    />
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
      <Button on:click={exit} color='danger'>Cancelar</Button>
    </Col>
    <Col class="text-center" xs="6">
      <Button color='success' type="submit">Submit</Button>
    </Col>
  </Row>
</Form>

<style>
</style>
