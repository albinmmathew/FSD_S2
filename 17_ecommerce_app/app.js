const USERS_KEY = 'vibe_users';
const CURRENT_USER_KEY = 'vibe_currentUser';
const PRODUCTS_KEY = 'vibe_products';
const CART_KEY = 'vibe_cart';
const STORE_VERSION = '2.2';

let currentView = 'home';

function initializeData() {
    const savedVersion = localStorage.getItem('store_version');

    if (savedVersion !== STORE_VERSION) {
        localStorage.removeItem(PRODUCTS_KEY);
        localStorage.setItem('store_version', STORE_VERSION);
    }

    if (!localStorage.getItem(USERS_KEY)) {
        localStorage.setItem(USERS_KEY, JSON.stringify([
            { id: 1, username: 'admin', password: 'password', role: 'admin' },
            { id: 2, username: 'user', password: 'password', role: 'user' }
        ]));
    }
    if (!localStorage.getItem(PRODUCTS_KEY)) {
        localStorage.setItem(PRODUCTS_KEY, JSON.stringify([
            {
                id: 1,
                name: 'Fender Stratocaster',
                price: 95000,
                description: 'The legendary electric guitar used by icons, featuring three single-coil pickups.',
                image: 'https://images.unsplash.com/photo-1550291652-6ea9114a47b1?w=600&q=80',
                stock: 5
            },
            {
                id: 2,
                name: 'Yamaha Digital Piano',
                price: 52000,
                description: 'A professional digital piano with weighted action and premium grand piano sound.',
                image: 'https://images.unsplash.com/photo-1552422535-c45813c61732?w=600&q=80',
                stock: 3
            },
            {
                id: 3,
                name: 'Shure SM7B Vocal Mic',
                price: 38000,
                description: 'The industry standard for professional podcasting, broadcasting, and vocal recording.',
                image: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=600&q=80',
                stock: 12
            }
        ]));
    }
}

// Routing system
function navigate(viewName, params = {}) {
    document.querySelectorAll('.spa-section').forEach(sec => sec.classList.remove('active'));
    const target = document.getElementById(`view-${viewName}`);
    if (target) {
        target.classList.add('active');
    }
    currentView = viewName;

    const user = getCurrentUser();
    if ((viewName === 'cart') && !user) {
        alert("Please login first.");
        return navigate('login');
    }
    if (viewName === 'manage-product' && (!user || user.role !== 'admin')) {
        return navigate('home');
    }

    renderNavbar();

    if (viewName === 'home') renderHomeProducts();
    if (viewName === 'products') renderProducts();
    if (viewName === 'cart') renderCart();
    if (viewName === 'manage-product') prepareManageForm(params.id);
}

// Authentication functions
function getCurrentUser() {
    return JSON.parse(localStorage.getItem(CURRENT_USER_KEY) || 'null');
}

function handleLogin(e) {
    e.preventDefault();
    const u = document.getElementById('login-user').value;
    const p = document.getElementById('login-pass').value;
    const users = JSON.parse(localStorage.getItem(USERS_KEY));
    const user = users.find(x => x.username === u && x.password === p);

    if (user) {
        localStorage.setItem(CURRENT_USER_KEY, JSON.stringify({ id: user.id, username: u, role: user.role }));
        document.getElementById('login-form').reset();
        navigate('home');
    } else {
        const err = document.getElementById('login-error');
        err.textContent = "Invalid credentials";
        err.style.display = 'block';
    }
}

function handleRegister(e) {
    e.preventDefault();
    const u = document.getElementById('reg-user').value;
    const p = document.getElementById('reg-pass').value;
    const p2 = document.getElementById('reg-confirm').value;
    const r = document.getElementById('reg-role').value;

    const err = document.getElementById('reg-error');
    if (p !== p2) return (err.style.display = 'block', err.textContent = "Passwords don't match");

    const users = JSON.parse(localStorage.getItem(USERS_KEY));
    if (users.find(x => x.username === u)) return (err.style.display = 'block', err.textContent = "User exists");

    const newUser = { id: Date.now(), username: u, password: p, role: r };
    users.push(newUser);
    localStorage.setItem(USERS_KEY, JSON.stringify(users));
    localStorage.setItem(CURRENT_USER_KEY, JSON.stringify({ id: newUser.id, username: u, role: r }));

    document.getElementById('register-form').reset();
    navigate('home');
}

function logout() {
    localStorage.removeItem(CURRENT_USER_KEY);
    navigate('login');
}

// Navbar and UI rendering
function renderNavbar() {
    const user = getCurrentUser();
    const cartCount = getCart().filter(i => user ? i.userId === user.id : false).reduce((a, c) => a + c.quantity, 0);

    let links = `
        <li class="nav-item"><a class="nav-link" href="#" onclick="navigate('home')">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#" onclick="navigate('products')">Shop</a></li>
    `;

    if (user) {
        if (user.role === 'admin') {
            links += `<li class="nav-item"><a class="nav-link" href="#" onclick="navigate('manage-product')">Manage Inventory</a></li>`;
        }
        links += `
            <li class="nav-item"><a class="nav-link" href="#" onclick="navigate('cart')">Cart <span class="badge bg-secondary">${cartCount}</span></a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="logout()">Logout (${user.username})</a></li>
        `;
    } else {
        links += `
            <li class="nav-item"><a class="nav-link" href="#" onclick="navigate('login')">Login</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="navigate('register')">Join Now</a></li>
        `;
    }
    document.getElementById('nav-links').innerHTML = links;
}

function getProducts() {
    return JSON.parse(localStorage.getItem(PRODUCTS_KEY) || '[]');
}

function renderHomeProducts() {
    const pList = getProducts().slice(0, 3);
    const container = document.getElementById('home-products');
    if (container) {
        container.innerHTML = pList.map(p => buildProductCard(p)).join('');
    }
}

function renderProducts() {
    const user = getCurrentUser();
    const isAdmin = user && user.role === 'admin';
    const actions = document.getElementById('admin-actions');
    if (actions) {
        actions.innerHTML = isAdmin ? `<button onclick="navigate('manage-product')" class="btn btn-material-secondary">Add New Instrument</button>` : '';
    }

    const pList = getProducts();
    const container = document.getElementById('products-list');
    if (container) {
        if (!pList.length) container.innerHTML = `<h4 class="text-muted w-100 text-center py-5">No items found</h4>`;
        else container.innerHTML = pList.map(p => buildProductCard(p, isAdmin)).join('');
    }
}

function buildProductCard(p, isAdmin = false) {
    let adminUI = isAdmin ? `
        <div class="mt-2 d-flex gap-2">
            <button class="btn btn-sm btn-outline-primary flex-fill" onclick="navigate('manage-product', {id: ${p.id}})">Edit</button>
            <button class="btn btn-sm btn-outline-danger flex-fill" onclick="deleteProduct(${p.id})">Delete</button>
        </div>` : '';

    return `
    <div class="col-md-4 col-lg-3">
        <div class="card card-material h-100">
            <img src="${p.image}" class="card-img-top dynamic-img">
            <div class="card-body d-flex flex-column">
                <h5 class="card-title text-truncate">${p.name}</h5>
                <p class="text-primary fw-bold fs-5 mb-1">₹${parseFloat(p.price).toLocaleString('en-IN')}</p>
                <p class="small text-muted mb-2">Stock: ${p.stock}</p>
                <p class="card-text text-muted flex-grow-1" style="font-size:0.8rem;">${p.description}</p>
                <button class="btn btn-material w-100 mt-auto" onclick="addToCart(${p.id})">Add to Cart</button>
                ${adminUI}
            </div>
        </div>
    </div>`;
}

// Cart management
function getCart() {
    return JSON.parse(localStorage.getItem(CART_KEY) || '[]');
}

function addToCart(pid) {
    const user = getCurrentUser();
    if (!user) { alert("Please login"); return navigate('login'); }

    let cart = getCart();
    const prod = getProducts().find(p => p.id == pid);
    if (!prod) return;

    const item = cart.find(c => c.productId == pid && c.userId == user.id);
    if (item) item.quantity++;
    else cart.push({ userId: user.id, productId: pid, quantity: 1, name: prod.name, price: prod.price, image: prod.image });

    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    renderNavbar();
    alert("Instrument added to cart!");
}

window.updateQty = function (pid, change) {
    const user = getCurrentUser();
    let cart = getCart();
    const item = cart.find(c => c.productId == pid && c.userId == user.id);
    if (item) {
        item.quantity += change;
        if (item.quantity <= 0) cart = cart.filter(c => c !== item);
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
        renderCart();
        renderNavbar();
    }
}

function renderCart() {
    const user = getCurrentUser();
    const userCart = getCart().filter(c => c.userId === user.id);
    const container = document.getElementById('cart-items');

    if (!userCart.length) {
        if (container) container.innerHTML = `<h4 class="text-muted p-5 text-center">Your cart is empty</h4>`;
        document.getElementById('cart-subtotal').textContent = "₹0.00";
        document.getElementById('cart-tax').textContent = "₹0.00";
        document.getElementById('cart-total').textContent = "₹0.00";
        return;
    }

    let subtotal = 0;
    container.innerHTML = userCart.map(c => {
        const itemTotal = c.price * c.quantity;
        subtotal += itemTotal;
        return `
        <div class="card card-material mb-3 p-3">
            <div class="row align-items-center">
                <div class="col-3"><img src="${c.image}" class="img-fluid rounded" style="height:60px; object-fit:cover;"></div>
                <div class="col-4">
                    <h6 class="mb-1">${c.name}</h6>
                    <small class="text-muted">₹${parseFloat(c.price).toLocaleString('en-IN')}</small>
                </div>
                <div class="col-3 d-flex align-items-center">
                    <button class="btn btn-sm" onclick="updateQty(${c.productId}, -1)">-</button>
                    <span class="px-2 fw-bold">${c.quantity}</span>
                    <button class="btn btn-sm" onclick="updateQty(${c.productId}, 1)">+</button>
                </div>
                <div class="col-2 text-primary fw-bold">₹${itemTotal.toLocaleString('en-IN')}</div>
            </div>
        </div>`;
    }).join('');

    const tax = subtotal * 0.08;
    document.getElementById('cart-subtotal').textContent = `₹${subtotal.toLocaleString('en-IN')}`;
    document.getElementById('cart-tax').textContent = `₹${tax.toLocaleString('en-IN')}`;
    document.getElementById('cart-total').textContent = `₹${(subtotal + tax).toLocaleString('en-IN')}`;
}

function handleCheckout() {
    const user = getCurrentUser();
    let cart = getCart();
    const uCart = cart.filter(c => c.userId === user.id);
    if (!uCart.length) return alert("Cart empty");

    alert("Order successful! Your music journey begins.");
    cart = cart.filter(c => c.userId !== user.id);
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    navigate('home');
}

// Product management (Admin)
function prepareManageForm(id) {
    const form = document.getElementById('manage-product-form');
    if (!form) return;
    form.reset();
    document.getElementById('prod-id').value = '';
    document.getElementById('manage-title').textContent = 'Add New Instrument';
    document.getElementById('manage-btn').textContent = 'Add Instrument';

    if (id) {
        const p = getProducts().find(x => x.id == id);
        if (p) {
            document.getElementById('manage-title').textContent = 'Edit Instrument';
            document.getElementById('manage-btn').textContent = 'Update Instrument';
            document.getElementById('prod-id').value = p.id;
            document.getElementById('prod-name').value = p.name;
            document.getElementById('prod-price').value = p.price;
            document.getElementById('prod-image').value = p.image;
            document.getElementById('prod-stock').value = p.stock;
            document.getElementById('prod-desc').value = p.description;
        }
    }
}

function handleManageProduct(e) {
    e.preventDefault();
    const id = document.getElementById('prod-id').value;
    const p = {
        name: document.getElementById('prod-name').value,
        price: parseFloat(document.getElementById('prod-price').value),
        image: document.getElementById('prod-image').value,
        stock: parseInt(document.getElementById('prod-stock').value),
        description: document.getElementById('prod-desc').value
    };

    let products = getProducts();
    if (id) {
        p.id = parseInt(id);
        const idx = products.findIndex(x => x.id == id);
        if (idx !== -1) products[idx] = p;
    } else {
        p.id = Date.now();
        products.push(p);
    }

    localStorage.setItem(PRODUCTS_KEY, JSON.stringify(products));
    alert(id ? "Updated" : "Added");
    navigate('products');
}

window.deleteProduct = function (id) {
    if (!confirm("Delete?")) return;
    let products = getProducts().filter(p => p.id != id);
    localStorage.setItem(PRODUCTS_KEY, JSON.stringify(products));
    renderProducts();
}

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    initializeData();
    const loginForm = document.getElementById('login-form');
    if (loginForm) loginForm.addEventListener('submit', handleLogin);
    const regForm = document.getElementById('register-form');
    if (regForm) regForm.addEventListener('submit', handleRegister);
    const manageForm = document.getElementById('manage-product-form');
    if (manageForm) manageForm.addEventListener('submit', handleManageProduct);
    navigate('home');
});
