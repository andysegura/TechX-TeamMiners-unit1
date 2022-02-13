// Code by Ryan Winkelman

// declare variables
var addGuitars = document.querySelectorAll('.add-cart-guitar') // add to cart buttons
var addBass = document.querySelectorAll('.add-cart-bass')
var addDrums = document.querySelectorAll('.add-cart-drums')
var decreases = document.querySelectorAll('.decrease') // minus one quantity
var increases = document.querySelectorAll('.increases') // plus one quantity
var productsGuitar = [ // hardcoded products in list to be able to access them
    {
        name: 'Gibson',
        img: 'gibson.jpg',
        page: 'guitar.html',
        tag: 'gibson',
        price: 500,
        inCart: 0
    },
    {
        name: 'Fender',
        img: 'fender.jpg',
        page: 'guitar.html',
        tag: 'fender',
        price: 250,
        inCart: 0
    }
];
var productsBass =[
    {
        name: 'Ibanez',
        img: 'ibanez.jpg',
        page: 'bass.html',
        tag: 'ibanez',
        price: 300,
        inCart: 0
    },
    {
        name: 'Rougue',
        img: 'rougue.jpg',
        page: 'bass.html',
        tag: 'rougue',
        price: 120,
        inCart: 0
    }
];
var productsDrum =[
    {
        name: 'Yamaha',
        img: 'yamaha.jpg',
        page: 'drums.html',
        tag: 'yamaha',
        price: 320,
        inCart: 0
    },
    {
        name: 'Sidekick',
        img: 'sidekick.jpg',
        page: 'drums.html',
        tag: 'sidekick',
        price: 250,
        inCart: 0
    },
];

// event listener for guitars
for (let i = 0; i < addGuitars.length; i++){
    addGuitars[i].addEventListener('click', () =>{
        numProductsInCart(productsGuitar[i], false)
        totalCost(productsGuitar[i])
    })
}
// event listener for drums
for (let i = 0; i < addDrums.length; i++){
    addDrums[i].addEventListener('click', () =>{
        numProductsInCart(productsDrum[i], false)
        totalCost(productsDrum[i])
    })
}
// event listener for bass
for (let i = 0; i < addBass.length; i++){
    addBass[i].addEventListener('click', () =>{
        numProductsInCart(productsBass[i], false)
        totalCost(productsBass[i])
    })
}

function loadNumInCart(){
    //if page is refreshed this will display the count still
    let numItems = localStorage.getItem('numProductsInCart');
    if ( numItems ){
        document.getElementById("num").textContent = numItems;
    }
}

// this function will update the number of items in the cart
function numProductsInCart(product, decrease){
    let numItems = localStorage.getItem('numProductsInCart');
    numItems = parseInt(numItems); //will come as string change to int
    if(decrease){
        localStorage.setItem('numProductsInCart', numItems - 1); //decrease value that is in local storage
        document.querySelector('.pages span').textContent = numItems - 1;
    }
    else if ( numItems ){
        localStorage.setItem('numProductsInCart', numItems + 1); //increment what in cart by one
        document.querySelector('.pages span').textContent = numItems + 1;
    }
    else{
        localStorage.setItem('numProductsInCart', 1); // there isn't anything in the cart. this will add the first item and initialize the variable
        document.querySelector('.pages span').textContent = 1;
    }
    setItems(product);
}

// create a list of how much of each individual item is in cart
function setItems(product){
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems); // will come as JSON object convert to js object
    if (cartItems != null){ 
        // already something in the cart
        let productToAdd = product.tag;
        // if the current product we are trying to add is not in the cart yet
        if ( cartItems[productToAdd] == undefined ){
            cartItems = {
                ...cartItems,
                [productToAdd]: product
            }
        }
        cartItems[productToAdd];
    }
    else{
        // initialize array
        cartItems= {
            [product.tag]: product //index it by the tag in the product object
        }
    }
    cartItems[product.tag].inCart += 1; // increase the amount that is in the cart

    localStorage.setItem('productsInCart', JSON.stringify(cartItems));
}

// increase the total cost of the cart
function totalCost(product, decrease){
    let cost = localStorage.getItem('totalCost');
    if (decrease){ // removing item from cart
        cost = parseFloat(cost); // since it comes as a string
        localStorage.setItem('totalCost', cost - product.price);
    }
    else if (cost != null){ // adding item and there is already a value for cost
        cost = parseFloat(cost);
        localStorage.setItem('totalCost', product.price + cost)
    }
    else{
        localStorage.setItem('totalCost', product.price);
    }
}

// display what is in cart and write to the html file
function displayCart(){
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);
    let cost = localStorage.getItem('totalCost');
    let shoppingCart = document.getElementById("shopping-cart-items"); // this will say where we are writing to the html file

    //here is where the fun begins! lol
    if ( cartItems && shoppingCart ){ //if these aren't null
        shoppingCart.innerHTML = ``; // initialized to empty string
        Object.values(cartItems).map(item => {
            shoppingCart.innerHTML += `
            <div class="product">
                <ion-icon name="close-circle"></ion-icon>
                <a href="${item.page}"><img = src="images/${item.img}"></a>
                <span>${item.name}</span>

            </div>
            <div class="product-price">$${item.price}.00</div>
            <div class="product-quantity">
                <ion-icon class="decrease" name="remove-circle-outline"></ion-icon>
                <span>${item.inCart}</span>
                <ion-icon class="increase" name="add-circle-outline"></ion-icon>
            </div >
            <div class="product-total">
                <span>$${item.inCart * item.price}</span>
            </div>
            `;
        });
        shoppingCart.innerHTML += `
            <div class="basketTotalContainer">
                <h4 class= "basketTotalTitle">
                    Basket Total
                </h4>
                <h4 class="basketTotal">
                    $${cost}.00
                </h4>
        `;
    }
    // call event listeners
    changeQuantity(); //if the quantity of each item needs to be incremented
    removeItems(); // if item needs to be removed
}

// event listener for if quantity buttons are pushed
function changeQuantity(){
    let decrease = document.querySelectorAll('.decrease');
    let increase = document.querySelectorAll('.increase');
    let curProduct = ''; // will hold which product is being updated
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems); // change to js objects
    // event listner for both increase and decrease
    for (let i = 0; i < increase.length; i++){
        //both will be the same length
        decrease[i].addEventListener('click', ()=>{
            // goes from decrease element to parent class to price class to product class gets what is in span and removes all spaces and leading characters
            curProduct = decrease[i].parentElement.previousElementSibling.previousElementSibling.querySelector('span').textContent.toLocaleLowerCase().replace(/ /g, '').trim();
            if (cartItems[curProduct].inCart > 1){ // make sure there is more than one element
                cartItems[curProduct].inCart -= 1; // decrease by one
                numProductsInCart(cartItems[curProduct], true); // decrease products in cart
                totalCost(cartItems[curProduct], true);
                localStorage.setItem('productsInCart', JSON.stringify(cartItems));
                displayCart();
            }
        });
        increase[i].addEventListener('click', ()=>{
            curProduct = increase[i].parentElement.previousElementSibling.previousElementSibling.querySelector('span').textContent.toLocaleLowerCase().replace(/ /g, '').trim();
            // increase by one
            cartItems[curProduct].inCart += 1;
            numProductsInCart(cartItems[curProduct], false);
            totalCost(cartItems[curProduct], false);
            localStorage.setItem('productsInCart', JSON.stringify(cartItems));
            displayCart();
        });
    }
}
// use remove button in cart
function removeItems(){
    console.log('in function')
    let deleteButton = document.querySelectorAll('.product ion-icon');
    let numProducts = localStorage.getItem('numProductsInCart');
    let cost = localStorage.getItem('totalCost');
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);
    let productName;
    console.log(deleteButton.length)
    for (let i = 0; i < deleteButton.length; i++){
        deleteButton[i].addEventListener('click', () =>{
            console.log('remove item')
            productName = deleteButton[i].parentElement.textContent.toLocaleLowerCase().replace(/ /g, '').trim();
            // remove item
            localStorage.setItem('numProductsInCart', numProducts - cartItems[productName].inCart);
            localStorage.setItem('totalCost', cost - (cartItems[productName].inCart * cartItems[productName].price));

            delete cartItems[productName];
            localStorage.setItem('productsInCart', JSON.stringify(cartItems));
            displayCart();
            loadNumInCart();
        });
    }
}
loadNumInCart();
displayCart();