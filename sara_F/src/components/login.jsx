import React from 'react';
import './Login.css'; // estilos
import {useForm} from 'react-hook-form'
import {Datosinicio} from '../api/login_api'
import {useNavigate,Link} from 'react-router-dom'

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


    const onSubmit = handleSubmit( async data => {
        
        console.log(data)
        const rest= await Datosinicio(data);
        console.log(rest);
        navigate("/inicio")

    });

    return (
        <div className="login-container">
            <div className="login-box">
                

                <div className="left-section">
                   
                <div className="logo-container">
                    <img src="https://cdn.discordapp.com/attachments/1294805456174452746/1294805644624531497/yaxd.png?ex=670c593a&is=670b07ba&hm=ac2dc55f59f61c7f9a250ae550d9d411a323a43b6e6f097da104b2897cfa4e83&" alt="Logo" className="logo" />
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
                        <button type="submit" style={{ fontWeight: 'bold' }}>Iniciar Sesión</button>
                    </form>
                </div>

                {/* seccion derecha /(poner imagen o algo) */}
                <div className="right-section">{}
                    
                </div>
            </div>
        </div>
    );
};

export default Login;