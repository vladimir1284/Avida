<script>
	import Bar from "./Bar.svelte"
	import Clients from "./clients/Clients.svelte"
</script>

<Bar/>
<main>
	<Clients/>
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