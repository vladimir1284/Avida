
<script>
    import  {Table}  from 'sveltestrap'
    import ClientForm from './ClientForm.svelte'
    import { Button, Row, Col, Input, Container } from 'sveltestrap';
    import PlusThick from "svelte-material-icons/PlusThick.svelte";
    import {filterTable} from '../utils'
    import { onMount } from 'svelte';   
	import { clients } from '../stores.js';

    let openform = false
    let currentClient 
    let clientes
    let searchFilter = ""

    $:{filterTable(searchFilter, "clientsTable")}

    $:{clientes = Object.values($clients)}

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

    function edit_client(event){        
        currentClient = clientes[parseInt(event.target.id)]
        console.log(currentClient)
        openform = true
    }
    
</script>
  
{#if openform}
    <ClientForm client={currentClient} bind:openform={openform}/>
{:else}
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
            bind:value={searchFilter}
            />
        </Col>
    </Row>

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
                        <a href="tel:{client.phone}"> {#if client.phone}{client.phone}{/if}</a>
                        <a href="tel:{client.cel}"> {#if client.cel}{client.cel}{/if}</a>
                    </td>
                </tr>
            {/each}
        </tbody>
    </Table>
{/if}