import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Datosinicio } from '../api/login_api';
import { useNavigate, Link } from 'react-router-dom';
import logo from './images/logo.png';
import { toast } from 'react-toastify';
import styled from 'styled-components';

const LoginContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to right, #0049d6, #63d8d9);
`;

const LoginBox = styled.div`
  display: flex;
  background-color: white;
  padding: 0;
  border-radius: 105px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 800px;
  height: 490px;
`;

const LeftSection = styled.div`
  flex: 1;
  border-radius: 7px;
  background-color: white;
  padding: 60px;
`;

const LogoContainer = styled.div`
  text-align: center;
  justify-content: center;
  margin-bottom: -26px;
  margin-top: -30px;
`;

const Logo = styled.img`
  max-width: 127px;
  height: auto;
`;

const GradientText = styled.h2`
  font-family: 'Playwrite IS', sans-serif;
  font-size: 29px;
  text-align: center;
  background: linear-gradient(90deg, #16368d, #0087d6);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
`;

const Separator = styled.hr`
  border: none;
  height: 2px;
  background-color: #ccc;
  margin: 10px 0;
`;

const RightSection = styled.div`
  flex: 1;
  border-radius: 7px;
  background-color: #eeedfc;
  padding: 40px;
`;

const InputGroup = styled.div`
  margin-bottom: 17px;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 5px;
`;

const Input = styled.input`
  width: 90%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const ForgotPasswordLink = styled(Link)`
  text-align: center;
  display: block;
  margin-top: 24px;
  margin-bottom: 19px;
`;

const SubmitButton = styled.button`
  font-weight: bold;
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #00c5d6;
  color: #fff;
  cursor: pointer;

  &:hover {
    background-color: #2575fc;
  }
`;

const Message = styled.p`
  color: red;
`;

export function Login() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const navigate = useNavigate();
    const [message, setMessage] = useState();

    const onSubmit = handleSubmit(async (data) => {
        const rest = await Datosinicio(data);
        if (rest.status === 200) {
            toast.success("Bienvenido a SARA", { position: "top-center" });
            setTimeout(() => navigate("/"), 5000);
        } else if (rest.status === 401) {
            toast.success("Usuario inactivo");
        } else {
            setMessage("Usuario o contraseña incorrectos, inténtelo de nuevo");
        }
    });

    return (
        <LoginContainer>
            <LoginBox>
                <LeftSection>
                    <LogoContainer>
                        <Logo src={logo} alt="Logo" />
                    </LogoContainer>
                    <GradientText>Bienvenido!</GradientText>
                    <Separator />
                    <form onSubmit={onSubmit}>
                        <InputGroup>
                            <Label htmlFor="username">Usuario</Label>
                            <Input
                                type="text"
                                id="username"
                                placeholder="Ingrese su usuario"
                                {...register("usuario", { required: true })}
                            />
                        </InputGroup>
                        <InputGroup>
                            <Label htmlFor="password">Contraseña</Label>
                            <Input
                                type="password"
                                id="password"
                                placeholder="Ingrese su contraseña"
                                {...register("password", { required: true })}
                            />
                            <ForgotPasswordLink to="/contraseña">¿Olvidaste tu contraseña?</ForgotPasswordLink>
                        </InputGroup>
                        <SubmitButton type="submit">Iniciar Sesión</SubmitButton>
                    </form>
                    {message && <Message>{message}</Message>}
                </LeftSection>
                <RightSection />
            </LoginBox>
        </LoginContainer>
    );
}

export default Login;