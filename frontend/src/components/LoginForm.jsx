import "../styles/LoginForm.css"
import { useState } from "react";
export default function LoginForm({onSwitchToRegister, loginSucces}){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    async function VerifySucces(e){
        e.preventDefault()
        // Appele a l'APi pour cette ligne
        const result = true
        if(result === false){
            setError("Nom d'utilisateur ou mot de passe incorect") 
        }
        else{
            loginSucces(result)
        }
    }
    return(
        <div>

            {error && <div className="error-message">{error}</div>}
            <form onSubmit={VerifySucces} className="body-form">
                <label>Adresse e-mail</label>
                <input 
                type="text"
                 placeholder="nom@domaine.com"
                 value={username}
                 onChange={(e) => setUsername(e.target.value)}/>
                <label>Mot de passe</label>
                <input 
                type="text"
                placeholder="votre mot de passe"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                 />
                <button type="submit" className="ConnexionButton">Se connecter</button>
            </form>
            <div className="divider-container">
                <div className="divider-line"></div>
                <span className="divider-text">ou</span>
                <div className="divider-line"></div>
            </div>
            <div>
                <button onClick={onSwitchToRegister} className="switch-button">
                    Inscrivez-vous Ici
                </button>
            </div>
        </div>
    )
}