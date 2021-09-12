
<script>
    import  {Table}  from 'sveltestrap'
    import {clientes} from '../backend'
    import ClientForm from './ClientForm.svelte'
    import { Button, Row, Col, Input } from 'sveltestrap';
    import PlusThick from "svelte-material-icons/PlusThick.svelte";

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

    function edit_client(event){        
        currentClient = clientes[parseInt(event.target.id)]
        console.log(currentClient)
        openform = true
    }
    function filterTable() {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("searchInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("clientsTable");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            const row = tr[i].getElementsByTagName("td")
            txtValue = ""
            // Collect all the text in a row
            for(var k= 0; k< row.length; k++){
                txtValue += row[k].textContent || row[k].innerText
            }
            // Remove acents
            txtValue = txtValue.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
            if (row) {                
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }       
        }
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
        <Col class="text-right" xs="8">
            <Input id="searchInput"
            type="text"
            placeholder="Buscar.."
            on:keyup={filterTable}
            style="max-width: 500px;"
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
                    <td>{client.cel}</td>
                </tr>
            {/each}
        </tbody>
    </Table>
{/if}