import { useState } from "react"
import LoginForm from "../components/LoginForm"
import RegisterForm from "../components/RegisterForm"
import logo from '../assets/Spotify_logo.png'
import '../styles/LoginForm.css'

export default function AuthPage(){
    const [isLoginView, setIsLoginView] = useState(true)
    const [registerSucces, setRegisterSucces] = useState(false)

    return(
        <div>
            <div className="auth-header">
                <img src={logo} alt="logo" className="auth-logo"/>
                <p className="auth-title">Connecter-vous pour commencer à écouter</p>
            </div>
            {registerSucces && isLoginView && (
                <div className="success-message">
                  Inscription réussie ! Vous pouvez maintenant vous connecter.
                   </div>
            )}
            
            {
                isLoginView ? (
                    <LoginForm onSwitchToRegister={
                        () => {
                            setIsLoginView(false)
                            setRegisterSucces(false)
                        }
                    }/>
                ) : (
                    <RegisterForm onSwitchToLogin={() => setIsLoginView(true)}
                    onRegisterSucces={() => setRegisterSucces(true)}/>
                )
            }
        </div>
    )
}