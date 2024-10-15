import {useForm} from 'react-hook-form'
import {RecoverPassword} from '../api/login_api'
import {useNavigate,Link} from 'react-router-dom'



export function RestorePassword(){

    const {register, handleSubmit,formState:{
        errors
    }} = useForm();
    
    //Permite hacer el redirecionamiento de la pagina sin recargas necesarias 
    const navigate = useNavigate();


    const onSubmit = handleSubmit( async data => {
        
        console.log(data)
        const rest= await RecoverPassword(data);
        console.log(rest);
        navigate("/inicio")

    });
    return(
        <div>
            <form onSubmit={onSubmit}>

                <h1>Recuperar Contraseña</h1>

                
                <label htmlFor="username">usuario</label>
                <input type="text" id="username" placeholder="Ingrese su usuario" {...register("usuario",{required:true})} />
                <label htmlFor="email">Correo electronico</label>
                <input type="text"  placeholder='Ingrese Correo'{...register("correo",{required:true})} />
                <button type="submit" style={{ fontWeight: 'bold' }}>Enviar correo</button>
                  


            </form>
        </div>
    )
}
export default RestorePassword