// Filter element rows
export function filterTable(searchInput, filterTabl) {
    const input = document.getElementById(searchInput);
    input.addEventListener('keyup', function(e) {
        var filter, table, tr, i, txtValue;
        filter = input.value.toUpperCase();
        table = document.getElementById(filterTabl);
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
    }, false);
}
 