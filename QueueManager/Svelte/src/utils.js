import { base_url } from './stores.js';

// Filter element rows
export function filterTable(searchFilter, filterTabl) {
    var filter, table, tr, i, txtValue;
    
    filter = searchFilter.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase();
    table = document.getElementById(filterTabl);
    if (table){
        tr = table.getElementsByTagName("tr");
        for (i = 1; i < tr.length; i++) {
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
}

// Ascynchronusly fetch data from backend
export function fetch_data(data_name, url, data_store){
    fetch(base_url + url)
    .then(response => {
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
        throw new TypeError("Oops, we haven't got JSON!");
        }
        return response.json();
    })
    .then(data => {
        data_store.set(data[data_name]);
    })
    .catch(error => console.error(error));
}