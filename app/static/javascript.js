(function (win, doc) {
  'use strict'
  
  if (doc.querySelector('.btnDelEmpresa')) {
    let btnDelEmpresa = doc.querySelectorAll('.btnDelEmpresa')
    
    for (let i of btnDelEmpresa) {
      i.addEventListener('click', function (event) {
        if (confirm('Deseja apagar esta empresa?')) {
          return true
        } else {
          event.preventDefault()
        }
      })
    }
  }

  if (doc.querySelector('.btnDelProduto')) {
    let btnDelProduto = doc.querySelectorAll('.btnDelProduto')
    
    for (let i of btnDelProduto) {
      i.addEventListener('click', function (event) {
        if (confirm('Deseja apagar este produto?')) {
          return true
        } else {
          event.preventDefault()
        }
      })
    }
  }
  
  // Formulário de produto
  if (doc.querySelector('#form-produto')) {
    let form = doc.querySelector('#form-produto')
    let url_parts = form.action.split('/')
    function sendForm(event) {
      event.preventDefault()
      let data = new FormData(form)
      let ajax = new XMLHttpRequest()
      let token = doc.querySelectorAll('input')[0].value
      ajax.open('POST', form.action)
      ajax.setRequestHeader('X-CSRF-TOKEN', token)
      ajax.onreadystatechange = function () {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let result = doc.querySelector('#result')
          result.innerHTML = 'Operação realizada com sucesso!'
          result.classList.add('alert')
          result.classList.add('alert-success')
          setTimeout(function (){
            window.location.href = '/empresa/' + url_parts[url_parts.length-2];          
          }, 1500);
        }
      }
      ajax.send(data)
      form.reset()
    }
    
    form.addEventListener('submit', sendForm, false)
  }

  // Formulário de empresa
  if (doc.querySelector('#form-empresa')) {
    let form = doc.querySelector('#form-empresa')
    
    function sendForm(event) {
      event.preventDefault()
      let data = new FormData(form)
      let ajax = new XMLHttpRequest()
      let token = doc.querySelectorAll('input')[0].value
      ajax.open('POST', form.action)
      ajax.setRequestHeader('X-CSRF-TOKEN', token)
      ajax.onreadystatechange = function () {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let result = doc.querySelector('#result')
          result.innerHTML = 'Operação realizada com sucesso!'
          result.classList.add('alert')
          result.classList.add('alert-success')
          setTimeout(function (){
            window.location.href = '/empresas';          
          }, 1500);
        }
      }
      ajax.send(data)
      form.reset()
    }
    
    form.addEventListener('submit', sendForm, false)
  }

})(window, document)