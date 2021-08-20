// Я удалил график

// За что график (((

// Иконочки
var food = "<img src='../../static/img/restaurant_black_24dp.svg'>";
var enter = "<img src='../../static/img/sports_esports_black_24dp.svg'>";
var pets = "<img src='../../static/img/pets_black_24dp.svg'>";
var tax = "<img src='../../static/img/request_quote_black_24dp.svg'>";
var travels = "<img src='../../static/img/map_black_24dp.svg'>";
var clothes = "<img src='../../static/img/checkroom_black_24dp.svg'>";
var transport = "<img src='../../static/img/commute_black_24dp.svg'>";
var medicine = "<img src='../../static/img/local_hospital_black_24dp.svg'>";
var other = "<img src='../../static/img/shopping_cart_black_24dp.svg'>";

var len = $("td").filter(function() {return(this.id == "icon");}).length;

for(var i = 0; i <= len; i++){
    if($($(".icon")[i]).html() == '<div class="category"></div>FOOD'){
        $($(".category")[i]).append(food);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>ENTER'){
        $($(".category")[i]).append(enter);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>PETS'){
        $($(".category")[i]).append(pets);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>TAX'){
        $($(".category")[i]).append(tax);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>TRAVELS'){
        $($(".category")[i]).append(travels);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>CLOTHES'){
        $($(".category")[i]).append(clothes);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>TRANS'){
        $($(".category")[i]).append(transport);
    }
    else if($($(".icon")[i]).html() == '<div class="category"></div>MEDICINE'){
        $($(".category")[i]).append(medicine);
    }
    else{
        $($(".category")[i]).append(other);
    }
}
function resize(){
    // Эта шляпа короче выравнивает левую колонку что бы не было пустот
    var num_of_tables = $("tr").filter(function() {return(this.id == "num_of_tables");}).length;

    // len - кол-во элементов в таблицах
    // num_of_tables - кол-во таблиц

    if(window.screen.height < 1000 && len >= 3 && num_of_tables > 1){
        document.getElementById("left-column").style.height = "auto";
    }
    else{
        document.getElementById("left-column").style.height = "100vh";
    }
}
resize();

window.addEventListener('resize', change_screen_size);
function change_screen_size(){
    resize();
}


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