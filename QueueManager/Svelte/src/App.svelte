<script>
	import Bar from "./Bar.svelte"
	import Clients from "./clients/Clients.svelte"
	import Orders from "./orders/Orders.svelte"
	import { clients, orders, base_url } from './stores.js';
    import { onMount } from 'svelte';  

	let view = "orders"


    // Get clients
    onMount(() => {
		fetch(base_url + 'get_clients/')
			.then(response => {
				const contentType = response.headers.get('content-type');
				if (!contentType || !contentType.includes('application/json')) {
				throw new TypeError("Oops, we haven't got JSON!");
				}
				return response.json();
			})
			.then(data => {
				clients.set(data.clients);
			})
			.catch(error => console.error(error));
		fetch(base_url + 'get_orders/')
			.then(response => {
				const contentType = response.headers.get('content-type');
				if (!contentType || !contentType.includes('application/json')) {
				throw new TypeError("Oops, we haven't got JSON!");
				}
				return response.json();
			})
			.then(data => {
				orders.set(data.orders);
			})
			.catch(error => console.error(error));
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