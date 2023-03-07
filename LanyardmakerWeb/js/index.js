


let params = new URLSearchParams(location.search);
params.get('id')
//print the value of the name parameter

id = params.get('id');
//fetch json data from http://localhost:9000/api/getprog/(parameter)
fetch(`http://localhost:9000/api/getprog/${id}`)
.then(response => response.json())
.then(data => {
    //print data
    console.log(data);
    let table = document.getElementById('tableBody');
    //loop through data
    data.forEach(element => {
      let tr = document.createElement('tr');
        //put data in table on page
        tr.innerHTML = `<td>${element.naam}</td>
        <td>${element.tijdslot}</td>
        <td>${element.spreker}</td>
        <td>${element.locatie}</td>
        <td>${element.dag}</td>`;
        table.appendChild(tr);
    });


})
.catch(err => {
    console.log(err);
});




