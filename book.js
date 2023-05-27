function book(p_page)
{
    // 构造函数
    this.left = 0
    this.right = 1
    this.max_page = p_page
    this.next_page = function()
    {
        this.left +=1
        this.right = this.left +1
        console.log("翻页",this)
    }
    this.priv_page = function()
    {
        this.left -=1
        this.right = this.right +1
        console.log("翻页",this)
    }
    this.jump_to = function(p_page)
    {
        this.left = p_page
    }
}