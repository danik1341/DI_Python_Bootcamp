const API_KEY = "afdb3b50151c04b14d2c3958";
const fromCurrencySelect = document.getElementById("fromCurrency");
const toCurrencySelect = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertBtn = document.getElementById("convertBtn");
const switchBtn = document.getElementById("switchBtn");
const resultOutput = document.getElementById("result");

const fetchCurrencies = async () => {
  const response = await fetch(
    `https://v6.exchangerate-api.com/v6/${API_KEY}/codes`
  );
  const data = await response.json();

  data.supported_codes.forEach((currencyInfo) => {
    const currencyCode = currencyInfo[0];
    const currencyName = currencyInfo[1];

    const fromOption = document.createElement("option");
    fromOption.value = currencyCode;
    fromOption.textContent = currencyName;
    fromCurrencySelect.appendChild(fromOption);

    const toOption = document.createElement("option");
    toOption.value = currencyCode;
    toOption.textContent = currencyName;
    toCurrencySelect.appendChild(toOption);
  });
};

const convertCurrencies = async () => {
  const fromCurrency = fromCurrencySelect.value;
  const toCurrency = toCurrencySelect.value;
  const amount = amountInput.value;

  const response = await fetch(
    `https://v6.exchangerate-api.com/v6/${API_KEY}/pair/${fromCurrency}/${toCurrency}/${amount}`
  );
  const data = await response.json();

  resultOutput.textContent = data.conversion_result;
};

convertBtn.addEventListener("click", convertCurrencies);
switchBtn.addEventListener("click", () => {
  const temp = fromCurrencySelect.value;
  fromCurrencySelect.value = toCurrencySelect.value;
  toCurrencySelect.value = temp;
  convertCurrencies();
});

fetchCurrencies();
