const inventory = {
  Smartphone: { quantidade: 10, preco: 800 },
  Notebook: { quantidade: 5, preco: 2500 },
  "Fone Bluetooth": { quantidade: 20, preco: 150 },
};

const stockList = document.getElementById("stockList");
const stockForm = document.getElementById("stockForm");
const productSelect = document.getElementById("product");
const actionSelect = document.getElementById("action");
const quantityInput = document.getElementById("quantity");
const status = document.getElementById("status");

function populateProducts() {
  Object.keys(inventory).forEach((product) => {
    const option = document.createElement("option");
    option.value = product;
    option.textContent = product;
    productSelect.appendChild(option);
  });
}

function renderInventory() {
  stockList.innerHTML = "";

  Object.entries(inventory).forEach(([product, info]) => {
    const item = document.createElement("li");
    item.className = "stock-item";
    item.innerHTML = `
      <div>
        <strong>${product}</strong>
        <span>R$ ${info.preco.toLocaleString("pt-BR")} por unidade</span>
      </div>
      <strong>${info.quantidade} un.</strong>
    `;
    stockList.appendChild(item);
  });
}

function updateStatus(message) {
  status.textContent = message;
}

stockForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const product = productSelect.value;
  const action = actionSelect.value;
  const quantity = Number(quantityInput.value);

  if (action === "add") {
    inventory[product].quantidade += quantity;
    updateStatus(`Você adicionou ${quantity} unidade(s) de ${product}.`);
  } else {
    if (inventory[product].quantidade >= quantity) {
      inventory[product].quantidade -= quantity;
      updateStatus(`Você removeu ${quantity} unidade(s) de ${product}.`);
    } else {
      updateStatus(`Estoque insuficiente para ${product}.`);
      return;
    }
  }

  renderInventory();
  quantityInput.value = 1;
});

populateProducts();
renderInventory();
updateStatus("A página está pronta para usar. Escolha um produto e uma ação.");
