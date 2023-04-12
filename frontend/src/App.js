import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react';


function App() {

  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  axios.get("http://127.0.0.1:8000/mockdata/").then((res)=>{
  console.log(res.data);
  //setUsername(res.data.username);
  //setPassword(res.data.password)
})

  return (
    <div className="App">
      {username}
      {password}
    </div>
  );
}

export default App;
