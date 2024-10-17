import {useForm} from 'react-hook-form'
import {RecoverPassword} from '../api/login_api'
import {useNavigate,Link} from 'react-router-dom'
import { toast, ToastContainer } from 'react-toastify';
import './restore.password.css'



ToastContainer
export function RestorePassword(){

    const {register, handleSubmit,formState:{
        errors
    }} = useForm();
    
    //Permite hacer el redirecionamiento de la pagina sin recargas necesarias 
    const navigate = useNavigate();

    const onSubmit = handleSubmit(async (data) => {
        console.log(data);
    
        try {
            const rest = await RecoverPassword(data);
            console.log(rest);
    
            // Redirigir si la respuesta es exitosa
            if (rest.status === 200) {

                toast.success("Bienvenido a SARA", { position: "top-center" });
                setTimeout(() =>{
                    navigate("/");
                },5000)
                
            } else {
                toast.error(rest.request, { position: "top-center" });
            }
        } catch (error) {
            toast.error("Error al recuperar la contraseña", { position: "top-center" });
        }
    });

    const Volver = ()=>{
        navigate("/")
    }
    return(
        
        <div className='contaner-restore'>
            <div className='request-password'>
                <form onSubmit={onSubmit}>
                    
                    <header>
                        <h1>Recuperar Contraseña</h1>
                    </header>
                    <article>
                        <p>Indicar usuarios para el cambio de contraseña</p>
                        
                    </article>

                    <div className='input'>

                        <label htmlFor="username"><b>Usuario</b></label>
                        <input type="text" id="username" placeholder="Ingrese su usuario" {...register("usuario",{required:true})} />
                        
                        <label htmlFor="email"><b>Correo electronico</b></label>
                        <input type="text"  placeholder='Ingrese Correo'{...register("correo",{required:true})} />
                    </div>
                   
                    <div className='button-group'>

                        <button type="submit" style={{ fontWeight: 'bold' }} onClick={onSubmit}
                        >Enviar correo</button>

                        <button type='submit'onClick={Volver}
                        >Cancelar</button>

                    </div>
                </form>
                <ToastContainer/>

            </div>

        </div>
    )
}
export default RestorePassword