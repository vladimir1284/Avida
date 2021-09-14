
<script>
    import  {Table}  from 'sveltestrap'
    import OrderForm from './OrderForm.svelte'
    import { Button, Row, Col, Input } from 'sveltestrap';
    import PlusThick from "svelte-material-icons/PlusThick.svelte";
    import Pencil from "svelte-material-icons/Pencil.svelte";
    import Cancel from "svelte-material-icons/Cancel.svelte";
    import Check from "svelte-material-icons/Check.svelte";
    import {filterTable} from '../utils'
    import { onMount } from 'svelte';   
	import { clients, orders } from '../stores.js';
    import { get } from 'svelte/store'
    var { DateTime } = require('luxon');

    let pedidos

    $:{
        pedidos = Object.values($orders)
        console.log(pedidos)
    }


    let openform = false
    let currentOrder
    let orderToEdit 
    let currentIndex = 1

    
    // Search event handler
    onMount(() => {
        currentOrder = pedidos[0]
        console.log(currentOrder)
		filterTable("orderSearchInput", "ordersTable")
	});
    

    function add_order(){
        orderToEdit = {
                        "client": null,
                        "lts": 20,
                        "available": null
                        }
        openform = true
    }

    function deliver_order(event){
        
    }

    function cancel_order(event){
        
    }

    function view_order(event){
        currentIndex = parseInt(event.target.id) + 1    
        currentOrder = pedidos[currentIndex-1]
    }

    function edit_order(event){    
        // Use current order values
        orderToEdit = currentOrder   
        openform = true
    }
</script>

{#if openform}
    <OrderForm order={orderToEdit} bind:openform={openform}/>
{:else}
    <Row>
        <Col xs="3">
            <h3>Pedidos</h3>
        </Col>
        <Col xs="1">
            <h3><Button on:click={add_order} color="primary"><PlusThick color="white" /></Button></h3>
        </Col>
        <Col class="text-right" xs={{ size: 6, offset: 2 }}>
            <Input id="orderSearchInput"
            type="text"
            placeholder="Buscar.."
            style="max-width: 500px;"
            />
        </Col>
    </Row>
    <hr class="mt-0 mb-4">


    {#if currentOrder !== undefined}
        <Col xs="12">    
            #{currentIndex}: <b> {currentOrder.lts}L </b> - {get(clients)[currentOrder.client].name} <br>
        </Col>   
        <Row>
            <Col xs="2">
                <a href="tel:{get(clients)[currentOrder.client].phone}">{#if get(clients)[currentOrder.client].phone}{get(clients)[currentOrder.client].phone}{/if}</a>
            </Col>
            <Col xs={{ size: 2, offset: 1 }} >
                <a href="tel:{get(clients)[currentOrder.client].cel}"> {#if get(clients)[currentOrder.client].cel}{get(clients)[currentOrder.client].cel}{/if}</a>
            </Col>   
            <Col xs={{ size: 1, offset: 1 }}>
                <Button on:click={deliver_order} color="primary"><Check color="white" /></Button> 
            </Col>
            <Col xs={{ size: 1, offset: 1 }}>
                <Button on:click={edit_order} color="primary"><Pencil color="white" /></Button>
            </Col>
            <Col xs={{ size: 1, offset: 1 }}>
                <Button on:click={cancel_order} color="danger"><Cancel color="white" /></Button> 
            </Col>
        </Row>
        <Row>
            <Col xs="4">
                Pedido a las <b>{DateTime.fromISO(currentOrder.created).setZone('local').toFormat('hh:mma')}</b>
            </Col>
            <Col xs="8">
                {get(clients)[currentOrder.client].address}
            </Col>
        </Row>
        <hr class="mt-0 mb-4">
    {/if}

    <Table striped responsive id="ordersTable">
        <thead>
        <tr>
            <th>#</th>
            <th>Hora</th>
            <th>Nombre</th>
            <th class="text-center">Cantidad</th>
        </tr>
        </thead>
        <tbody>
            {#if get(clients) !== {}}
                {#each pedidos as pedido, index}
                    <tr>
                        <th scope="row"><Button on:click={view_order} id={index}>{index+1}</Button></th>
                        <td>{DateTime.fromISO(pedido.created).setZone('local').toFormat('hh:mma')}</td>
                        <td on:click={view_order} id={index}>{get(clients)[pedido.client].name}</td>
                        <td class="text-center">{pedido.lts}L</td>
                    </tr>
                {/each}
            {/if}
        </tbody>
    </Table>
{/if}