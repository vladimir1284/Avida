
<script>
    import  {Table}  from 'sveltestrap'
    import {clientes} from '../backend'
    import ClientForm from './ClientForm.svelte'
    import { Button, Row, Col, Input, Container } from 'sveltestrap';
    import PlusThick from "svelte-material-icons/PlusThick.svelte";
    import {filterTable} from '../utils'
    import { onMount } from 'svelte';   

    let openform = false
    let currentClient 

    function add_client(){
        currentClient = {
                          name: "",
                          cel: "",
                          phone: "",
                          address: "",
                          fbid: ""
                        }
        openform = true
    }

    // Search event handler
    onMount(() => {
        filterTable("searchInput", "clientsTable")
    });

    function edit_client(event){        
        currentClient = clientes[parseInt(event.target.id)]
        console.log(currentClient)
        openform = true
    }
    
</script>
  
{#if openform}
    <ClientForm client={currentClient} bind:openform={openform}/>
{:else}
<Container>
    <Row>
        <Col xs="3">
            <h3>Clientes</h3>
        </Col>
        <Col xs="1">
            <h3><Button on:click={add_client} color="primary"><PlusThick color="white" /></Button></h3>
        </Col>
        <Col class="text-right" xs={{ size: 6, offset: 2 }}>
            <Input id="searchInput"
            type="text"
            placeholder="Buscar.."
            style="max-width: 500px;"
            />
        </Col>
    </Row>
</Container>

    <Table striped responsive id="clientsTable">
        <thead>
        <tr>
            <th>Nombre</th>
            <th>Dirección</th>
            <th>Teléfono</th>
        </tr>
        </thead>
        <tbody>
            {#each clientes as client, index}
                <tr>
                    <td on:click={edit_client} id={index}>{client.name}</td>
                    <td>{client.address}</td>
                    <td>
                        <a href="tel:{client.phone}"> {client.phone}</a>
                        <a href="tel:{client.cel}"> {client.cel}</a>
                    </td>
                </tr>
            {/each}
        </tbody>
    </Table>
{/if}