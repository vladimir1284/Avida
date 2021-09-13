<script>
	import Bar from "./Bar.svelte"
	import Clients from "./clients/Clients.svelte"
	import Orders from "./orders/Orders.svelte"

	let view = "orders"
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