import {BrowserRouter, Routes,Route} from 'react-router-dom';
import {Recuperacontraseña} from './pages/Recuperacontraseña'
import {Inicio} from './pages/principal'
import  Login from './components/login'


function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/contraseña" element={<Recuperacontraseña/>}/>
        <Route path='/inicio' element={<Inicio/>}/>
      </Routes>
    
    
    </BrowserRouter>
  )
}

export default App;

