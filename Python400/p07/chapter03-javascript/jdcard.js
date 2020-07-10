function selectAllOrUnselectAll(ele) {
    var flag = ele.checked;
    var sels = document.getElementsByName("sel");
    alert(ele + sels);
    for (var i in sels) {
        sels[i].checked = true;
        alert(ele + flag);
    }
}

function plusNum(ele) {
    var pre = ele.previousElementSibling;
    pre.value = Number(pre.value) + 1;
    sumPrice(ele, pre.value)
}

function subNum(ele) {
    var next = ele.nextElementSibling;
    next.value = Number(next.value) - 1;
    sumPrice(ele, next.value)
}

function sumPrice(ele, num) {
    var price = ele.parentElement.previousElementSibling.innerHTML;
    ele.parentElement.nextElementSibling.innerHTML = "￥" + Number(price.slice(1)) * Number(num);
}