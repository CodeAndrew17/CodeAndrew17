import axios, {Axios} from 'axios'

export const Datosinicio = (login) => {
    return axios.post('http://127.0.0.1:8000/access/login/',login)
}

export const RecoverPassword = (datos)=>{
    return axios.post('http://127.0.0.1:8000/access/solicitarpassword/',datos)
}


