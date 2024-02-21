class Reservations{
    async post(data:any) {
        try{
            const request = await fetch(`http://127.0.0.1:8000/reservaciones/${id}`, {
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
                }
            );
            if(request){
                return true;
            }else{
                return false;
            }
        }catch(err){
            console.error('Ha ocurrido un error ' + err );
        }
    }

    async get(){
        try{

        }catch(err){
            console.error('Ha ocurrido un error ' + err)
        }
    }
}