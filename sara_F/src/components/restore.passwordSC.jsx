import {useForm} from 'react-hook-form'
import {RecoverPassword} from '../api/login_api'
import {useNavigate,Link} from 'react-router-dom'
import { toast, ToastContainer } from 'react-toastify';
import styled from 'styled-components';

const ContainerRestore = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(to right, #0049D6, #63d8d9);
`;

const RequestPassword = styled.div`
    background: white;
    padding: 80px;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 400px;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    font-family: Helvetica, sans-serif, Arial;
`;

const Header = styled.header`
    text-align: center;
    line-height: 100px;
    margin-top: -100px;
`;

const InputGroup = styled.div`
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    margin-left: 2px;
    gap: 10px;
`;

const StyledInput = styled.input`
    width: 90%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
`;

const ButtonGroup = styled.div`
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-top: 20px;
`;

const StyledButton = styled.button`
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    flex: 1;
    font-weight: bold;
    background-color: #00c5d6;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    
    &:hover {
        background-color: #2575fc;
    }
`;

export function RestorePassword() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const navigate = useNavigate();

    const onSubmit = handleSubmit(async (data) => {
        console.log(data);

        try {
            const rest = await RecoverPassword(data);
            console.log(rest);

            if (rest.status === 200) {
                toast.success("Bienvenido a SARA", { position: "top-center" });
                setTimeout(() => {
                    navigate("/");
                }, 5000);
            } else {
                toast.error(rest.request, { position: "top-center" });
            }
        } catch (error) {
            toast.error("Error al recuperar la contraseña", { position: "top-center" });
        }
    });

    const Volver = () => {
        navigate("/");
    };

    return (
        <ContainerRestore>
            <RequestPassword>
                <form onSubmit={onSubmit}>
                    <Header>
                        <h1>Recuperar Contraseña</h1>
                    </Header>
                    <article>
                        <h4>Ingrese su usuario y correo electrónico</h4>
                    </article>

                    <InputGroup>
                        <label htmlFor="username"><b>Usuario</b></label>
                        <StyledInput type="text" id="username" placeholder="Ingrese su usuario" {...register("usuario", { required: true })} />
                        
                        <label htmlFor="email"><b>Correo electrónico</b></label>
                        <StyledInput type="text" placeholder="Ingrese su correo electrónico" {...register("correo", { required: true })} />
                    </InputGroup>

                    <ButtonGroup>
                        <StyledButton type="submit" onClick={onSubmit}>Enviar correo</StyledButton>
                        <StyledButton type="button" onClick={Volver}>Cancelar</StyledButton>
                    </ButtonGroup>
                </form>
                <ToastContainer />
            </RequestPassword>
        </ContainerRestore>
    );
}

export default RestorePassword;