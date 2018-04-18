socket = new WebSocket("ws://" + window.location.host + "/chat/");

socket.onmessage = function(e) {
    var data=JSON.parse(e.data);
    

    let template = `
<div class="panel panel-info">
    <div class= "company_name panel-heading">
      ${ data.name }
    </div>
    <div class="description panel-body ">
     
     ${data.position }</br>
      ${ data.location } </br>
      ${ data.stipend }/month </br>
      Number of positions : ${ data.no_of_positon } </br> 
    
    </div>

  <div class="panel-footer detail-container" align="center">
    <button type="button" onclick="change( '${ data.name }' , '${ data.description }' ,'${ data.id }'  )" class="btn btn-primary "  data-toggle="modal" data-target="#detailModal" >Details</button>  
  </div>
</div>`;

    let div = document.createElement('div');
    div.setAttribute('class', "col-sm-3");
    div.innerHTML = template;
    var element = document.getElementById("row_div");
    element.appendChild(div);    
}

function hi(){ 
  if (socket.readyState == WebSocket.OPEN) socket.send('');
}

function change(name,desc,companyId){

document.getElementById("modalBody").innerHTML=desc;
document.getElementById("modalTitle").innerHTML=name;
document.getElementById("formNum").value=companyId;

}

function fillForm(companyId){
window.open("google.com");
}