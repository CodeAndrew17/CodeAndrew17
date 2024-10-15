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
    const notify = () => {
        toast.success("Notificación Básica",{position:'top-center'})
            
    };
    const onSubmit = handleSubmit( async data => {
        
        console.log(data)
        const rest= await RecoverPassword(data);
        console.log(rest);
        navigate("/inicio")

    });
    const Volver = ()=>{
        navigate("/")
    }
    return(
        
        <div className='contaner-restore'>
            <div className='request-password'>
                <form onSubmit={onSubmit}>
                    <div className='title'>
                        <h1>Recuperar Contraseña</h1>
                    </div>

                    <div className='input-group'>

                        <label htmlFor="username"><b>Usuario</b></label>
                        <input type="text" id="username" placeholder="Ingrese su usuario" {...register("usuario",{required:true})} />
                        
                        <label htmlFor="email"><b>Correo electronico</b></label>
                        <input type="text"  placeholder='Ingrese Correo'{...register("correo",{required:true})} />
                    </div>
                   
                    <div className='button-group'>

                        <button type="submit" style={{ fontWeight: 'bold' }} onClick={notify}
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