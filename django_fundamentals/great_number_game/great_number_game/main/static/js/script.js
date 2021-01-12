
$(document).ready(function(){

var select = '';
for (i=1;i<=100;i++){
    select += '<option val=' + i + '>' + i + '</option>';
}
$('#guess').html(select);

console.log('ready');
  
        
});
