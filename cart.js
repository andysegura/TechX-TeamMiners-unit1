// full disclosure I used a youtube tutorial here: https://www.youtube.com/watch?v=B20Getj_Zk4
// I did not copy any code.  I followed the video with a seperate project I made.  Then applied what I learned to make this file
// I am not familiar with java script so I may have broken a few java script rules/conventions
// By Ryan Winkelman

// declare variables
let add = document.querySelectorAll('.add-cart') // add to cart buttons
let decreases = document.querySelectorAll('.decrease') // minus one quantity
let increases = document.querySelectorAll('.increases') // plus one quantity
let products = [ // hardcoded products in list to be able to access them
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
    },
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
        tag: 'gibson',
        price: 120,
        inCart: 0
    },
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
        tag: 'fender',
        price: 250,
        inCart: 0
    },
];

// event listener for add to cart button
for (let i = 0; i < add.length; i++){
    add[i].addEventListener('click', () =>{
        numProductsInCart(products[i], 1)
        totalCost(products[i])
    })
}

function loadNumInCart(){
    //if page is refreshed this will display the count still
    let numItems = localStorage.getItem('numProductsInCart');
    if (numItems != null){
        document.querySelector('.pages span').textContent = numItems;
    }
}

// this function will update the number of items in the cart
function numProductsInCart(product, decrease){
    let numItems = localStorage.getItem('numProductsInCart');
    numItems = parseInt(numItems); //will come as string change to int
    if(decrease){
        localStorage.setItem('numProductsInCart', numItems - 1); //decrease value that is in local storage
        loadNumInCart();
    }
    else if (numItems != 1){
        localStorage.setItem('numProductsInCart', numItems + 1); //increment what in cart by one
        loadNumInCart();
    }
    else{
        localStorage.setItem('numProductsInCart', 1); // there isn't anything in the cart. this will add the first item and initialize the variable
        loadNumInCart();
    }
    setItems(product);
}

// create a list of how much of each individual item is in cart
function setItems(product){
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems); // will come as JSON object convert to js object
    if (cartItems != null && cartItems[product.tag] == undefined){ 
        // already something in the cart
        // if the current product we are trying to add is not in the cart yet
        cartItems = {
            ...cartItems,
            [product.tag]: product
        }
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
    let cost = localStorage.get('totalCost');
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
    let products = document.querySelector('.products-in-cart'); // this will say where we are writing to the html file

    //here is where the fun begins! lol
    if (cartItems && products){ //if these aren't null
        products.innerHTML = ''; // initialized to empty string
        Object.values(cartItems).map(product => {
            products += `
            <div class="product">
                <ion-icon name="close-circle"></ion-icon>
                <a href="index.html"><img = src="images/${item.img}"></a>
                <span>${item.name}</span>

            </div>
            <div class="price">$${item.price}.00</div>
            <div class="quantity">
                <ion-icon class="decrease" name="remove-circle-outline"></ion-icon>
                <span>${item.inCart}</span>
                <ion-icon class="increase" name="add-circle-outline"></ion-icon>
            </div >
            <div class="total">
                <span>$${item.inCart * item.price}</span>
            </div>
            `;
        });
        productContainer.innerHTML += `
            <div class="basketTotalContainer">
                <h4 class= "basketTotalTitle">
                    Basket Total
                </h4>
                <h4 class="basketTotal">
                    $${cartCost}.00
                </h4>
        `
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
    let deleteButton = document.querySelectorAll('.product ion-icon');
    let numProducts = localStorage.getItem('numProductsInCart');
    let cost = localStorage.getItem('totalCost');
    let cartItems = localStorage.getItem('productsInCart');
    let productName;

    for (let i = 0; i < deleteButton.length; i++){
        deleteButton[i].addEventListener('click', () =>{
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