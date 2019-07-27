$(function(){
    document.addEventListener('click', (event)=>{
        if(event.target.classList.contains('emptyButton')){
            alert('This button doesn\'t have action, yet...');
        }
        if(event.target.classList.contains('listDisk')){
            console.log("Pushed");
            window.location.href = 'http://127.0.0.1:5000/disk';
            // $.ajax({
            //     method: "GET",
            //     url: '/disk',
            //     data:{},
            //     success:()=>{
            //         window.location.href = 'http://127.0.0.1:5000/disk';
            //     }
            // });
        }
        if(event.target.classList.contains('folder')){
            //console.log(event.target.getAttribute('data-id'));
                window.location.href = 'http://127.0.0.1:5000/folder/' + event.target.getAttribute('data-id');

            // $.ajax({
            //     method: "GET",
            //     url: '/folder/' + event.target.getAttribute('data-id'),
            //     data:{},
            //     success:()=>{
            //          window.location.href = 'http://127.0.0.1:5000/folder/' + event.target.getAttribute('data-id');
            //         console.log('succesfull!');
            //
            //     }
            // });
        }
    });
});