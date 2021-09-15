<script>
	import {
	  Collapse,
	  Navbar,
	  NavbarToggler,
	  NavbarBrand,
	  Nav,
	  NavItem,
	  NavLink,
	  Dropdown,
	  DropdownToggle,
	  DropdownMenu,
	  DropdownItem
	} from 'sveltestrap';
  
	let isOpen = false;
  
  export let view
  
	function handleUpdate(event) {
	  isOpen = event.detail.isOpen;
	}
  function pedidos(){
    view = "orders"
  }
  function dashboard(){    
    view = "dashboard"
  }
  function clientes(){    
    view = "clients"
  }
  </script>
  
  
<Navbar color="light" light expand="md">
    <NavbarBrand on:click={dashboard}><img src="img/logo.png" alt="Ávida"></NavbarBrand>
    <NavbarToggler on:click={() => (isOpen = !isOpen)} />
    <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
        <Nav class="ms-auto" navbar>
        <NavItem>
            <NavLink on:click={pedidos}>Pedidos</NavLink>
        </NavItem>
        <NavItem>
            <NavLink on:click={clientes}>Clientes</NavLink>
        </NavItem>
        <Dropdown nav inNavbar>
            <DropdownToggle nav caret>Opciones</DropdownToggle>
            <DropdownMenu end>
            <DropdownItem><a href="/accounts/logout/">Salir</a></DropdownItem>
            <!-- <DropdownItem>Option 2</DropdownItem>
            <DropdownItem divider />
            <DropdownItem>Reset</DropdownItem> -->
            </DropdownMenu>
        </Dropdown>
        </Nav>
    </Collapse>
</Navbar>
