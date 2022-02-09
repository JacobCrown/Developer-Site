
// get search form and page links
let search_form = document.getElementById('search_form')
let page_links = document.getElementsByClassName('page-link')

// ensure serach form exists
if(search_form){
    for(let i=0; page_links.length > i; i++){
        page_links[i].addEventListener('click', function (e) {
            e.preventDefault()

            // get the data atribute
            let page = this.dataset.page

            // add hidden serach input to form
            search_form.innerHTML += `<input value=${page} name="page" hidden />`

            // submit form
            search_form.submit()
        })
    }
}
