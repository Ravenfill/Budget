// Я удалил график

 
if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
    document.getElementById("add-purchase").value = "+ добавить покупку";
}
else{
    function on_mouse_enter(){
        document.getElementById("add-purchase").value = "+ добавить покупку";
    }
    
    function on_mouse_exit(){
        document.getElementById("add-purchase").value = "+";
    }
}


const layer = document.getElementById('layer');

function open_adding_menu(){
  layer.style.display = 'block';
}

layer.addEventListener('click', (e) => {
  if (e.target === layer) {
    layer.style.display = 'none';
  }
});

document.getElementById("close_img").hidden = true;
document.getElementById("mobile-nav").hidden = true;
function open_mobile_menu(){
    document.getElementById("mobile-nav").hidden = false;
    document.getElementById("close_img").hidden = false;
    document.getElementById("open_img").hidden = true;
}

function close_mobile_menu(){
    document.getElementById("mobile-nav").hidden = true;
    document.getElementById("close_img").hidden = true;
    document.getElementById("open_img").hidden = false;
}

// куки
function checkCookies(){
    let cookieDate = localStorage.getItem('cookieDate');
    let cookieNotification = document.getElementById('cookie_notification');
    let cookieBtn = cookieNotification.querySelector('.cookie_accept');

   
    if( !cookieDate || (+cookieDate + 31536000000) < Date.now() ){
        cookieNotification.classList.add('show');
    }

   
    cookieBtn.addEventListener('click', function(){
        localStorage.setItem( 'cookieDate', Date.now() );
        cookieNotification.classList.remove('show');
    })
}
checkCookies();