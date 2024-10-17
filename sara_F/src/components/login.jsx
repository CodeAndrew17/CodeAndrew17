import React, { useState } from 'react';
import './Login.css'; // estilos
import {useForm} from 'react-hook-form'
import {Datosinicio} from '../api/login_api'
import {useNavigate,Link} from 'react-router-dom'
import logo from './images/logo.png'
import { toast } from 'react-toastify';

export function Login(){
    /*
        Permite el guardar los Datos de inputs Tempramente en moria "register"
        permite hacer el llamdo de esos Datos gurdados "handleSubmit"
    */
    const {register, handleSubmit,formState:{
        errors
    }} = useForm();
    
    //Permite hacer el redirecionamiento de la pagina sin recargas necesarias 
    const navigate = useNavigate();

    const [message, setMessage] = useState()


    const onSubmit = handleSubmit(async (data) => {
        console.log(data);
       
        const rest = await Datosinicio(data);  
        console.log(rest);
    
        if (rest.status === 200) {

                toast.success("Bienvenido a SARA", { position: "top-center" });
                setTimeout(() =>{
                    navigate("/");
                },5000)

        } 
        else if (rest.status === 401) {
            toast.success("Usuario inactivo");
            } 
        else{
            setMessage("Usuario o contraseña incorrectos, inténtelo de nuevo");
            }

    });
    

    return (
        <div className="login-container">
            <div className="login-box">
                

                <div className="left-section">
                   
                <div className="logo-container">
                    <img src={logo} alt="Logo" className="logo" />
                </div>

                <h2 className="gradient-text">Bienvenido!</h2>

                    <hr className="separator" />

                    <form onSubmit={onSubmit}>
                        <div className="input-group">
                            <label htmlFor="username">Usuario</label>
                            <input type="text" id="username" placeholder="Ingrese su usuario" {...register("usuario",{required:true})} />
                        </div>
                        <div className="input-group">
                            <label htmlFor="password">Contraseña</label>
                            <input type="password" id="password" placeholder='Ingrese su contraseña' {...register("password", {required:true} )} />

                            <div className="forgot-password">
                            <Link  className= "forgot-password-link"  to={"/contraseña"}>¿Olvidaste tu contraseña?</Link>
                        </div>

                        </div>
                        <button type="submit" style={{ fontWeight: 'bold' }}
                        onClick={onSubmit}
                        >
                          
                            Iniciar Sesión
                        </button>
                    </form>
                    {message && <p className="message">{message}</p>}
                </div>

                {/* seccion derecha /(poner imagen o algo) */}
                <div className="right-section">{}
                    
                </div>
            </div>
        </div>
    );
};

export default Login;