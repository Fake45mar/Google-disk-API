$(function(){
    document.addEventListener('click', (event)=>{
        if(event.target.classList.contains('emptyButton')){
            alert('This button doesn\'t have action, yet...');
        }
        if(event.target.classList.contains('listDisk')){
            window.location.href = 'http://192.168.13.49:8000/disk';
        }
        if(event.target.classList.contains('folder')){
            window.location.href = 'http://192.168.13.49:8000/folder/' + event.target.getAttribute('data-id');
        }
    });
});