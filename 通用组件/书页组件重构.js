function Book()
{
    var index = 0
    var pageLabel = document.getElementById("pageLabel")
    var img = document.getElementById("book")
    this.priv = function()
    {
        index -=1
        console.log(index)
        pageLabel.innerText = "当前页码: " + index
        img.src = index + ".jpg"
        img.alt = "缺页"

    }
    this.next = function()
    {
        index +=1
        pageLabel.innerText = "当前页码：" + index
        img.src = index + ".jpg"
        img.alt = "缺页"
    }
    this.changePage = function()
    {
        index = page
        pageLabel.innerText = "当前页码：" + index
        img.src = index + ".jpg"
        img.alt = "缺页"
    }
}
var book = new Book()
var privButton = document.getElementById("privButton")
var nextButton = document.getElementById("nextButton")
var pageInput = document.getElementById("pageInput")
var jumpButton = document.getElementById("jumpButton")

privButton.onclick = book.priv
nextButton.onclick = book.next
jumpButton.onclick = function()
{
    page = pageInput.value
    book.changePage(page)
}
