function handleSearch() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    fetch(`/search?q=${input}`)
        .then(response => response.json())
        .then(data => showResults(data));
}

function showResults(results) {
    const resultList = document.getElementById('searchResults');
    resultList.innerHTML = '';
    results.forEach(result => {
        const li = document.createElement('li');
        li.textContent = result;
        resultList.appendChild(li);
    });
}
