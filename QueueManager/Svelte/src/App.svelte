<script>
	import Bar from "./Bar.svelte"
	import Clients from "./clients/Clients.svelte"
	import Orders from "./orders/Orders.svelte"
	import { clients, orders } from './stores.js';
    import { onMount } from 'svelte';  
    import {fetch_data} from './utils'

	let view = "orders"


    // Get clients
    onMount(() => {
		fetch_data('clients', 'get_clients/', clients);
		fetch_data('orders', 'get_orders/', orders);
	});
    
</script>

<Bar bind:view={view}/>
<main>
	{#if view == "orders"}
		<Orders/>
	{/if}
	{#if view == "clients"}
		<Clients/>
	{/if}
</main>

<style>
	main {
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>