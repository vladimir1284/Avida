<script>
    export let addElement
</script>

<div on:click={addElement} class="circle">
    <div class="circle-plus">
        <div class="vertical-plus"> 
        </div>  
    </div>
</div>

<style>
    .circle{       
            margin-top: 0.5em;
            height: 0.7em;
            width: 0.7em;
            border: 1px solid #004568;
            border-radius: 50%;
            display: inline-block;
            /* color: red; */
            background-color: #41a7b996;
        }
    .circle-plus{
        position: relative;
        background-color: #004568;
        width: 50%;
        height: 12.5%;
        left: 25%;
        top: 43.75%;
    }
    .vertical-plus{
        position: relative;
        background-color: #004568;
        width: 21.5%;
        height: 399%;
        left: 40.75%;
        top: -127.5%;
    }
</style>