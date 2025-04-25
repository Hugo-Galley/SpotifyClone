import { useState } from 'react';
import '../styles/LoginForm.css'

export default function RegisterForm({onSwitchToLogin, onRegisterSucces}){
        const [username, setUsername] = useState('');
        const [password, setPassword] = useState('');
        const [email, setEmail] = useState('')
        const [error, setError] = useState('');
    
        async function VerifySucces(e){
            e.preventDefault()
            // Appele a l'APi pour cette ligne
            const result = true
            if(result === false){
                setError("Nom d'utilisateur ou mot de passe incorect") 
            }
            else{
                onRegisterSucces(result)
                onSwitchToLogin()
            }
        }
    return(
        <div>
            {error && <div className="error-message">{error}</div>}
            <form onSubmit={VerifySucces} className="body-form-register">
                <label>Adresse e-mail</label>
                <input
                 type="text"
                placeholder="nom@domaine.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                  />

                <label>Mot de passe</label>
                <input
                type="text"
                placeholder="votre mot de passe"
                value={password}
                onChange={(e) => setPassword(e.target.value)}/>

                <label>Votre nom</label>
                <input
                type="text" 
                placeholder="nom utilisé dans l'application"
                value={username}
                onChange={(e) => setUsername(e.target.value)}/>

                <button type="submit" className="ConnexionButton">S'inscrire</button>
            </form>
            <div className="divider-container">
                <div className="divider-line"></div>
                <span className="divider-text">ou</span>
                <div className="divider-line"></div>
            </div>
            <div>
                <button onClick={onSwitchToLogin} className="switch-button">Retour à la connexion</button>
            </div>
        </div>
    )
}