<script>
    import { Button } from 'sveltestrap';
    import Pencil from "svelte-material-icons/Pencil.svelte";
    import TrashCan from "svelte-material-icons/TrashCan.svelte";
    import { Col, Container, Row } from 'sveltestrap'

    export let client
</script>

<h3>Cliente 
    <Button color="primary"><Pencil color="white" /></Button>
    <Button class="float-right"color="danger"><TrashCan color="white"/></Button>    
</h3>
<Row>client.name</Row>