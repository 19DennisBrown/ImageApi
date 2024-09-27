


const url = `http://localhost:8000/`

const collect= async ()=>{
  fetch(url)
    .then((res)=>{
      return res.json()
    })
    .then((data)=>{
      console.log(data)
    })
    return data
// const response = await fetch(url)
//  const data = await response.json()
//  console.log(data)
}
collect()

