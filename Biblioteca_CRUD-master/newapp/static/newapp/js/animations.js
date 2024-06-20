
function animateDeletion(rowId) {
    const row = document.getElementById(`row-${rowId}`);
    row.classList.add('animate-delete');
    setTimeout(() => {
        row.remove();
    }, 500);
}
