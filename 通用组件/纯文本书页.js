var index = 1
        var priv = document.getElementById("privButton")
        var next = document.getElementById("nextButton")
        var book = document.getElementsByClassName("paper")
        var view = document.getElementById("pageLable")
        next.onclick = function()
        {
            index +=1 
            var url = index +".html"
            const Http = new XMLHttpRequest()
            Http.open("GET",url)
            Http.send()
            Http.onreadystatechange = function()
            {
                // console.log(Http.responseText)
                // console.log(book.item(0))
                book.item(0).innerHTML = Http.responseText
                pageLabel.innerText = "当前页码：" + index
                // book.innerHtml = Http.responseText
            }
        }
        priv.onclick = function()
        {
            if(index >1)
            {
                index -=1
                if(index == 1)
                {
                    var url = "index.html"
                    window.open("index.html","_self")
                }
                else
                {
                    var url = index +".html"
                    const Http = new XMLHttpRequest()
                    Http.open("GET",url)
                    Http.send()
                    Http.onreadystatechange = function()
                    {
                        // console.log(Http.responseText)
                        // console.log(book.item(0))
                        book.item(0).innerHTML = Http.responseText
                        // book.innerHtml = Http.responseText
                    }
                }
                
                pageLabel.innerText = "当前页码：" + index
            }
        }