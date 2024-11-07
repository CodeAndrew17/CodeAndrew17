import {BrowserRouter, Routes,Route} from 'react-router-dom';
import {Recuperacontraseña} from './pages/Recuperacontraseña'
import {Inicio} from './pages/principal'
import  Login from './components/loginSC'
import { createGlobalStyle } from 'styled-components';


const GlobalStyle = createGlobalStyle`
    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 12px;
    }
`;

function App(){
  return(
  <>
    <GlobalStyle />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/contraseña" element={<Recuperacontraseña/>}/>
        <Route path='/inicio' element={<Inicio/>}/>
      </Routes>
    </BrowserRouter>
  </>
  );
}

export default App;

