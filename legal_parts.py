# Privacy, Terms and FAQ pages (4 languages)
import blog_parts as BL
L=['en','es','fr','it']
WA='https://wa.me/212659288638'; MAIL='moroccoroyaltrips0@gmail.com'
ML=f'<a href="mailto:{MAIL}">{MAIL}</a>'; WL=f'<a href="{WA}" target="_blank" rel="noopener">+212 659 288 638</a>'

UI={
'en':dict(lg_upd="Last updated: 3 November 2026",lg_pr_h="Privacy <em>Policy</em>",lg_tm_h="Terms &amp; <em>Conditions</em>",lg_fq_h="Frequently asked <em>questions</em>",
  lg_pr_c="Privacy Policy",lg_tm_c="Terms & Conditions",lg_fq_c="FAQ",lg_fq_p="Everything travellers usually ask us before booking a private tour in Morocco. Can’t find your answer? Write to us, we reply personally.",
  lg_bx_e="Questions?",lg_bx_h="Talk to our <em>team</em>",lg_bx_p="We reply personally, usually within a few hours, 7 days a week.",lg_bx_b="Contact us",lg_bx_w="WhatsApp",
  ft_faq="FAQ",ft_pr="Privacy Policy",ft_tm="Terms & Conditions"),
'es':dict(lg_upd="Última actualización: 3 de noviembre de 2026",lg_pr_h="Política de <em>privacidad</em>",lg_tm_h="Términos y <em>condiciones</em>",lg_fq_h="Preguntas <em>frecuentes</em>",
  lg_pr_c="Política de privacidad",lg_tm_c="Términos y condiciones",lg_fq_c="Preguntas frecuentes",lg_fq_p="Todo lo que los viajeros suelen preguntarnos antes de reservar un circuito privado en Marruecos. ¿No encuentras tu respuesta? Escríbenos y te respondemos personalmente.",
  lg_bx_e="¿Preguntas?",lg_bx_h="Habla con nuestro <em>equipo</em>",lg_bx_p="Respondemos personalmente, normalmente en pocas horas, los 7 días de la semana.",lg_bx_b="Contáctanos",lg_bx_w="WhatsApp",
  ft_faq="Preguntas frecuentes",ft_pr="Privacidad",ft_tm="Términos y condiciones"),
'fr':dict(lg_upd="Dernière mise à jour : 3 novembre 2026",lg_pr_h="Politique de <em>confidentialité</em>",lg_tm_h="Conditions <em>générales</em>",lg_fq_h="Questions <em>fréquentes</em>",
  lg_pr_c="Confidentialité",lg_tm_c="Conditions générales",lg_fq_c="FAQ",lg_fq_p="Tout ce que les voyageurs nous demandent avant de réserver un circuit privé au Maroc. Vous ne trouvez pas votre réponse ? Écrivez-nous, nous répondons personnellement.",
  lg_bx_e="Des questions ?",lg_bx_h="Parlez à notre <em>équipe</em>",lg_bx_p="Nous répondons personnellement, en général en quelques heures, 7 jours sur 7.",lg_bx_b="Nous contacter",lg_bx_w="WhatsApp",
  ft_faq="FAQ",ft_pr="Confidentialité",ft_tm="Conditions générales"),
'it':dict(lg_upd="Ultimo aggiornamento: 3 novembre 2026",lg_pr_h="Informativa sulla <em>privacy</em>",lg_tm_h="Termini e <em>condizioni</em>",lg_fq_h="Domande <em>frequenti</em>",
  lg_pr_c="Privacy",lg_tm_c="Termini e condizioni",lg_fq_c="FAQ",lg_fq_p="Tutto ciò che i viaggiatori ci chiedono prima di prenotare un tour privato in Marocco. Non trovi la risposta? Scrivici, ti rispondiamo di persona.",
  lg_bx_e="Domande?",lg_bx_h="Parla con il nostro <em>team</em>",lg_bx_p="Rispondiamo di persona, di solito entro poche ore, 7 giorni su 7.",lg_bx_b="Contattaci",lg_bx_w="WhatsApp",
  ft_faq="FAQ",ft_pr="Privacy",ft_tm="Termini e condizioni")}

def ul(*xs): return '<ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'

PR={
'en':[(None,f"<p>This policy explains what personal information MoroccoRoyalTrips collects when you contact us or book a trip, how we use it and how we protect it. We only ask for what we need to organise your journey.</p>"),
 ("1. Who we are",f"<p>MoroccoRoyalTrips is a local tour operator based in Morocco, organising private tours, day trips and desert experiences. For any question about your data, contact us at {ML} or on WhatsApp {WL}.</p>"),
 ("2. Information we collect","<p>When you fill in our contact form, write to us by email or WhatsApp, or book a tour, we may collect:</p>"+ul("Your name, email address and phone or WhatsApp number","Your travel dates, number of travellers, departure city and preferred tour","Information you choose to share to personalise your trip, such as dietary needs, mobility needs or a special occasion","Messages you send us")),
 ("3. How we use it",ul("To answer your questions and send you a personalised itinerary and quote","To organise and confirm your trip: accommodation, desert camps, transport, guides and activities","To contact you before and during your trip about practical details","To meet our accounting and legal obligations")+"<p>We do not send advertising newsletters without your consent.</p>"),
 ("4. Who we share it with","<p>We never sell or rent your personal information. We only share the details strictly necessary for your trip with the partners who deliver it, such as hotels, riads, desert camps, drivers and local guides. We may also disclose information if the law requires it.</p>"),
 ("5. How long we keep it","<p>We keep your information for as long as needed to prepare and carry out your trip, and afterwards only as long as required for accounting or legal reasons. You can ask us to delete it at any time, unless we have to keep it by law.</p>"),
 ("6. Security","<p>We take reasonable measures to protect your information against loss, misuse or unauthorised access, and only the members of our team who organise your trip can see it.</p>"),
 ("7. Cookies and browser storage","<p>Our website does not use advertising cookies. It only stores your preferred language in your browser so the site opens in the same language next time. Links to WhatsApp, Google Maps or Tripadvisor open those services, which have their own privacy policies.</p>"),
 ("8. Your rights",f"<p>You can ask to see, correct or delete the personal information we hold about you, or object to its use. Simply write to {ML} and we will reply as quickly as possible.</p>"),
 ("9. Changes to this policy","<p>We may update this policy from time to time. The date at the top of the page shows the latest version.</p>")],
'es':[(None,f"<p>Esta política explica qué datos personales recoge MoroccoRoyalTrips cuando nos contactas o reservas un viaje, cómo los usamos y cómo los protegemos. Solo pedimos lo necesario para organizar tu viaje.</p>"),
 ("1. Quiénes somos",f"<p>MoroccoRoyalTrips es un operador local con base en Marruecos que organiza circuitos privados, excursiones y experiencias en el desierto. Para cualquier pregunta sobre tus datos, escríbenos a {ML} o por WhatsApp al {WL}.</p>"),
 ("2. Datos que recogemos","<p>Cuando rellenas nuestro formulario, nos escribes por email o WhatsApp o reservas un circuito, podemos recoger:</p>"+ul("Tu nombre, email y número de teléfono o WhatsApp","Tus fechas de viaje, número de viajeros, ciudad de salida y circuito preferido","La información que decidas compartir para personalizar el viaje, como necesidades alimentarias, de movilidad o una ocasión especial","Los mensajes que nos envías")),
 ("3. Cómo los usamos",ul("Para responder a tus preguntas y enviarte un itinerario y presupuesto personalizados","Para organizar y confirmar tu viaje: alojamiento, campamentos, transporte, guías y actividades","Para contactarte antes y durante el viaje sobre detalles prácticos","Para cumplir nuestras obligaciones contables y legales")+"<p>No enviamos boletines publicitarios sin tu consentimiento.</p>"),
 ("4. Con quién los compartimos","<p>Nunca vendemos ni alquilamos tus datos. Solo compartimos los datos estrictamente necesarios con los colaboradores que hacen posible el viaje, como hoteles, riads, campamentos, conductores y guías locales. También podemos comunicarlos si la ley lo exige.</p>"),
 ("5. Cuánto tiempo los conservamos","<p>Conservamos tus datos el tiempo necesario para preparar y realizar el viaje y, después, solo el tiempo exigido por motivos contables o legales. Puedes pedirnos que los borremos en cualquier momento, salvo que la ley nos obligue a conservarlos.</p>"),
 ("6. Seguridad","<p>Tomamos medidas razonables para proteger tus datos frente a pérdidas, usos indebidos o accesos no autorizados, y solo los miembros del equipo que organizan tu viaje pueden verlos.</p>"),
 ("7. Cookies y almacenamiento del navegador","<p>Nuestra web no usa cookies publicitarias. Solo guarda en tu navegador el idioma que prefieres para que la web se abra en el mismo idioma la próxima vez. Los enlaces a WhatsApp, Google Maps o Tripadvisor abren esos servicios, que tienen sus propias políticas de privacidad.</p>"),
 ("8. Tus derechos",f"<p>Puedes pedir ver, corregir o borrar los datos que tenemos sobre ti, u oponerte a su uso. Escríbenos a {ML} y te responderemos lo antes posible.</p>"),
 ("9. Cambios en esta política","<p>Podemos actualizar esta política de vez en cuando. La fecha al principio de la página indica la versión más reciente.</p>")],
'fr':[(None,f"<p>Cette politique explique quelles données personnelles MoroccoRoyalTrips collecte lorsque vous nous contactez ou réservez un voyage, comment nous les utilisons et comment nous les protégeons. Nous ne demandons que ce qui est nécessaire pour organiser votre voyage.</p>"),
 ("1. Qui sommes-nous",f"<p>MoroccoRoyalTrips est un opérateur local basé au Maroc qui organise des circuits privés, des excursions et des expériences dans le désert. Pour toute question sur vos données, écrivez-nous à {ML} ou sur WhatsApp au {WL}.</p>"),
 ("2. Données collectées","<p>Lorsque vous remplissez notre formulaire, nous écrivez par e-mail ou WhatsApp, ou réservez un circuit, nous pouvons collecter :</p>"+ul("Votre nom, votre adresse e-mail et votre numéro de téléphone ou WhatsApp","Vos dates de voyage, le nombre de voyageurs, la ville de départ et le circuit souhaité","Les informations que vous choisissez de partager pour personnaliser le voyage : régime alimentaire, mobilité ou occasion spéciale","Les messages que vous nous envoyez")),
 ("3. Utilisation",ul("Répondre à vos questions et vous envoyer un itinéraire et un devis personnalisés","Organiser et confirmer votre voyage : hébergements, camps, transport, guides et activités","Vous contacter avant et pendant le voyage pour les détails pratiques","Respecter nos obligations comptables et légales")+"<p>Nous n’envoyons pas de newsletters publicitaires sans votre accord.</p>"),
 ("4. Partage","<p>Nous ne vendons ni ne louons jamais vos données. Nous transmettons uniquement les informations strictement nécessaires aux partenaires qui réalisent votre voyage : hôtels, riads, camps, chauffeurs et guides locaux. Nous pouvons aussi les communiquer si la loi l’exige.</p>"),
 ("5. Durée de conservation","<p>Nous conservons vos données le temps nécessaire pour préparer et réaliser votre voyage, puis uniquement le temps exigé pour des raisons comptables ou légales. Vous pouvez demander leur suppression à tout moment, sauf obligation légale de conservation.</p>"),
 ("6. Sécurité","<p>Nous prenons des mesures raisonnables pour protéger vos données contre la perte, l’usage abusif ou l’accès non autorisé, et seuls les membres de l’équipe qui organisent votre voyage y ont accès.</p>"),
 ("7. Cookies et stockage du navigateur","<p>Notre site n’utilise pas de cookies publicitaires. Il enregistre seulement votre langue préférée dans votre navigateur, afin que le site s’ouvre dans la même langue la prochaine fois. Les liens vers WhatsApp, Google Maps ou Tripadvisor ouvrent ces services, qui ont leurs propres politiques de confidentialité.</p>"),
 ("8. Vos droits",f"<p>Vous pouvez demander à consulter, corriger ou supprimer vos données, ou vous opposer à leur utilisation. Écrivez simplement à {ML} et nous vous répondrons au plus vite.</p>"),
 ("9. Modifications","<p>Nous pouvons mettre à jour cette politique de temps en temps. La date en haut de la page indique la version la plus récente.</p>")],
'it':[(None,f"<p>Questa informativa spiega quali dati personali raccoglie MoroccoRoyalTrips quando ci contatti o prenoti un viaggio, come li usiamo e come li proteggiamo. Chiediamo solo ciò che serve per organizzare il tuo viaggio.</p>"),
 ("1. Chi siamo",f"<p>MoroccoRoyalTrips è un tour operator locale con sede in Marocco che organizza tour privati, escursioni ed esperienze nel deserto. Per qualsiasi domanda sui tuoi dati scrivici a {ML} o su WhatsApp al {WL}.</p>"),
 ("2. Dati che raccogliamo","<p>Quando compili il modulo, ci scrivi via e-mail o WhatsApp o prenoti un tour, possiamo raccogliere:</p>"+ul("Nome, indirizzo e-mail e numero di telefono o WhatsApp","Date di viaggio, numero di viaggiatori, città di partenza e tour preferito","Le informazioni che scegli di condividere per personalizzare il viaggio, come esigenze alimentari, di mobilità o un’occasione speciale","I messaggi che ci invii")),
 ("3. Come li usiamo",ul("Per rispondere alle tue domande e inviarti un itinerario e un preventivo personalizzati","Per organizzare e confermare il viaggio: alloggi, campi, trasporti, guide e attività","Per contattarti prima e durante il viaggio per i dettagli pratici","Per rispettare gli obblighi contabili e legali")+"<p>Non inviamo newsletter pubblicitarie senza il tuo consenso.</p>"),
 ("4. Con chi li condividiamo","<p>Non vendiamo né affittiamo mai i tuoi dati. Condividiamo solo le informazioni strettamente necessarie con i partner che realizzano il viaggio, come hotel, riad, campi, autisti e guide locali. Possiamo inoltre comunicarli se la legge lo richiede.</p>"),
 ("5. Per quanto tempo li conserviamo","<p>Conserviamo i dati per il tempo necessario a preparare e svolgere il viaggio e, in seguito, solo per il tempo richiesto da motivi contabili o legali. Puoi chiederci di cancellarli in qualsiasi momento, salvo obblighi di legge.</p>"),
 ("6. Sicurezza","<p>Adottiamo misure ragionevoli per proteggere i tuoi dati da perdita, uso improprio o accesso non autorizzato, e solo i membri del team che organizzano il tuo viaggio possono vederli.</p>"),
 ("7. Cookie e memoria del browser","<p>Il nostro sito non usa cookie pubblicitari. Salva solo nel browser la lingua preferita, così il sito si apre nella stessa lingua la volta successiva. I link a WhatsApp, Google Maps o Tripadvisor aprono questi servizi, che hanno le proprie informative sulla privacy.</p>"),
 ("8. I tuoi diritti",f"<p>Puoi chiedere di vedere, correggere o cancellare i dati che conserviamo su di te, oppure opporti al loro uso. Scrivi a {ML} e ti risponderemo il prima possibile.</p>"),
 ("9. Modifiche","<p>Possiamo aggiornare questa informativa di tanto in tanto. La data in cima alla pagina indica la versione più recente.</p>")]}

TM={
'en':[(None,"<p>These terms apply to all private tours, day trips and activities organised by MoroccoRoyalTrips. By confirming a booking, you accept them. Please read them carefully, and ask us if anything is unclear.</p>"),
 ("1. Quotes and itineraries","<p>Every trip is tailor-made. After you contact us, we send you a written itinerary and a quote, with what is included and not included. Prices depend on the dates, the number of travellers, the season and the accommodation category you choose.</p>"),
 ("2. Booking and payment","<p>Your trip is confirmed once we receive the deposit and send you our written confirmation.</p>"+ul("The amount of the deposit depends on the tour and is stated in your quote","The balance is paid on arrival in Morocco","The accepted payment methods are explained in your quote")),
 ("3. What the price includes","<p>The price includes only the services listed as included in your itinerary, usually the private vehicle with driver, fuel, the accommodation and meals mentioned, and the activities described. Unless stated otherwise, it does not include international flights, travel insurance, entrance fees not mentioned, drinks, tips and personal expenses.</p>"),
 ("4. Changes to your booking",f"<p>If you wish to change your dates, the number of travellers or the itinerary, please tell us in writing as early as possible at {ML} or on WhatsApp. We will always do our best to adapt your trip; changes may affect the price, depending on availability.</p>"),
 ("5. Changes during the trip","<p>Weather, road conditions, local events or safety reasons can sometimes require us to change the order of visits, the route or an accommodation. In that case, we will always offer an equivalent alternative and keep you informed.</p>"),
 ("6. Passports, visas and insurance","<p>Each traveller is responsible for having a valid passport and, if required for their nationality, a visa for Morocco. We strongly recommend travel insurance covering medical expenses, repatriation and cancellation.</p>"),
 ("7. Health and activities","<p>Please tell us before the trip about any health condition, reduced mobility, pregnancy or dietary need, so we can adapt the itinerary. During activities such as camel rides, quad biking, sandboarding or hiking, travellers must follow the instructions of the guides and staff.</p>"),
 ("8. Our partners and responsibility","<p>We carefully select the hotels, riads, desert camps, drivers and guides we work with. We cannot be held responsible for events beyond our control, such as extreme weather, natural events, strikes, road closures or flight delays, but we will always help you find the best solution.</p>"),
 ("9. Respect and behaviour","<p>We ask all travellers to respect Moroccan laws, local customs, the people they meet and the environment. We may refuse to continue a service in case of dangerous or seriously disrespectful behaviour.</p>"),
 ("10. Contact",f"<p>For any question about these terms, write to {ML} or contact us on WhatsApp {WL}.</p>")],
'es':[(None,"<p>Estos términos se aplican a todos los circuitos privados, excursiones y actividades organizados por MoroccoRoyalTrips. Al confirmar una reserva, los aceptas. Léelos con atención y pregúntanos si algo no está claro.</p>"),
 ("1. Presupuestos e itinerarios","<p>Cada viaje es a medida. Tras contactarnos, te enviamos un itinerario y un presupuesto por escrito, con lo que está incluido y lo que no. Los precios dependen de las fechas, el número de viajeros, la temporada y la categoría de alojamiento elegida.</p>"),
 ("2. Reserva y pago","<p>Tu viaje queda confirmado cuando recibimos el depósito y te enviamos nuestra confirmación por escrito.</p>"+ul("El importe del depósito depende del circuito y se indica en tu presupuesto","El resto se paga a la llegada a Marruecos","Las formas de pago aceptadas se explican en tu presupuesto")),
 ("3. Qué incluye el precio","<p>El precio incluye solo los servicios indicados como incluidos en tu itinerario, normalmente el vehículo privado con conductor, el combustible, el alojamiento y las comidas mencionadas y las actividades descritas. Salvo que se indique lo contrario, no incluye vuelos internacionales, seguro de viaje, entradas no mencionadas, bebidas, propinas ni gastos personales.</p>"),
 ("4. Cambios en tu reserva",f"<p>Si quieres cambiar las fechas, el número de viajeros o el itinerario, avísanos por escrito lo antes posible en {ML} o por WhatsApp. Siempre haremos lo posible por adaptar tu viaje; los cambios pueden afectar al precio según la disponibilidad.</p>"),
 ("5. Cambios durante el viaje","<p>El tiempo, el estado de las carreteras, eventos locales o motivos de seguridad pueden obligarnos a veces a cambiar el orden de las visitas, la ruta o un alojamiento. En ese caso, siempre te ofreceremos una alternativa equivalente y te mantendremos informado.</p>"),
 ("6. Pasaportes, visados y seguro","<p>Cada viajero es responsable de tener un pasaporte válido y, si su nacionalidad lo requiere, un visado para Marruecos. Recomendamos encarecidamente un seguro de viaje que cubra gastos médicos, repatriación y cancelación.</p>"),
 ("7. Salud y actividades","<p>Infórmanos antes del viaje de cualquier problema de salud, movilidad reducida, embarazo o necesidad alimentaria, para adaptar el itinerario. Durante actividades como paseos en camello, quad, sandboard o senderismo, los viajeros deben seguir las instrucciones de los guías y del personal.</p>"),
 ("8. Nuestros colaboradores y responsabilidad","<p>Seleccionamos con cuidado los hoteles, riads, campamentos, conductores y guías con los que trabajamos. No podemos ser responsables de hechos ajenos a nuestro control, como tiempo extremo, fenómenos naturales, huelgas, cortes de carretera o retrasos de vuelos, pero siempre te ayudaremos a encontrar la mejor solución.</p>"),
 ("9. Respeto y comportamiento","<p>Pedimos a todos los viajeros que respeten las leyes marroquíes, las costumbres locales, a las personas que conozcan y el entorno. Podemos negarnos a continuar un servicio en caso de comportamiento peligroso o gravemente irrespetuoso.</p>"),
 ("10. Contacto",f"<p>Para cualquier pregunta sobre estos términos, escribe a {ML} o contáctanos por WhatsApp al {WL}.</p>")],
'fr':[(None,"<p>Ces conditions s’appliquent à tous les circuits privés, excursions et activités organisés par MoroccoRoyalTrips. En confirmant une réservation, vous les acceptez. Lisez-les attentivement et n’hésitez pas à nous poser vos questions.</p>"),
 ("1. Devis et itinéraires","<p>Chaque voyage est sur mesure. Après votre demande, nous vous envoyons un itinéraire et un devis écrits, précisant ce qui est inclus et non inclus. Les prix dépendent des dates, du nombre de voyageurs, de la saison et de la catégorie d’hébergement choisie.</p>"),
 ("2. Réservation et paiement","<p>Votre voyage est confirmé dès réception de l’acompte et envoi de notre confirmation écrite.</p>"+ul("Le montant de l’acompte dépend du circuit et figure dans votre devis","Le solde est réglé à votre arrivée au Maroc","Les moyens de paiement acceptés sont précisés dans votre devis")),
 ("3. Ce que comprend le prix","<p>Le prix comprend uniquement les prestations indiquées comme incluses dans votre itinéraire, en général le véhicule privé avec chauffeur, le carburant, les hébergements et repas mentionnés et les activités décrites. Sauf mention contraire, il ne comprend pas les vols internationaux, l’assurance voyage, les entrées non mentionnées, les boissons, les pourboires et les dépenses personnelles.</p>"),
 ("4. Modification de la réservation",f"<p>Si vous souhaitez modifier vos dates, le nombre de voyageurs ou l’itinéraire, prévenez-nous par écrit le plus tôt possible à {ML} ou sur WhatsApp. Nous ferons toujours de notre mieux pour adapter votre voyage ; les modifications peuvent faire varier le prix selon les disponibilités.</p>"),
 ("5. Changements pendant le voyage","<p>La météo, l’état des routes, des événements locaux ou des raisons de sécurité peuvent parfois nous obliger à modifier l’ordre des visites, l’itinéraire ou un hébergement. Nous vous proposerons alors toujours une alternative équivalente et vous tiendrons informés.</p>"),
 ("6. Passeports, visas et assurance","<p>Chaque voyageur est responsable de disposer d’un passeport valide et, si sa nationalité l’exige, d’un visa pour le Maroc. Nous recommandons vivement une assurance voyage couvrant les frais médicaux, le rapatriement et l’annulation.</p>"),
 ("7. Santé et activités","<p>Merci de nous signaler avant le départ tout problème de santé, mobilité réduite, grossesse ou besoin alimentaire, afin d’adapter l’itinéraire. Pendant les activités comme les balades à dromadaire, le quad, le sandboard ou la randonnée, les voyageurs doivent suivre les consignes des guides et du personnel.</p>"),
 ("8. Nos partenaires et responsabilité","<p>Nous sélectionnons avec soin les hôtels, riads, camps, chauffeurs et guides avec qui nous travaillons. Nous ne pouvons être tenus responsables d’événements indépendants de notre volonté, comme des conditions météo extrêmes, des phénomènes naturels, des grèves, des routes fermées ou des retards de vol, mais nous vous aiderons toujours à trouver la meilleure solution.</p>"),
 ("9. Respect et comportement","<p>Nous demandons à tous les voyageurs de respecter les lois marocaines, les coutumes locales, les personnes rencontrées et l’environnement. Nous pouvons refuser de poursuivre une prestation en cas de comportement dangereux ou gravement irrespectueux.</p>"),
 ("10. Contact",f"<p>Pour toute question sur ces conditions, écrivez à {ML} ou contactez-nous sur WhatsApp au {WL}.</p>")],
'it':[(None,"<p>Questi termini si applicano a tutti i tour privati, le escursioni e le attività organizzati da MoroccoRoyalTrips. Confermando una prenotazione li accetti. Leggili con attenzione e chiedici pure se qualcosa non è chiaro.</p>"),
 ("1. Preventivi e itinerari","<p>Ogni viaggio è su misura. Dopo il tuo contatto ti inviamo un itinerario e un preventivo scritti, con ciò che è incluso e non incluso. I prezzi dipendono dalle date, dal numero di viaggiatori, dalla stagione e dalla categoria di alloggio scelta.</p>"),
 ("2. Prenotazione e pagamento","<p>Il viaggio è confermato quando riceviamo l’acconto e ti inviamo la nostra conferma scritta.</p>"+ul("L’importo dell’acconto dipende dal tour ed è indicato nel preventivo","Il saldo si paga all’arrivo in Marocco","I metodi di pagamento accettati sono spiegati nel preventivo")),
 ("3. Cosa comprende il prezzo","<p>Il prezzo comprende solo i servizi indicati come inclusi nell’itinerario, di solito il veicolo privato con autista, il carburante, gli alloggi e i pasti menzionati e le attività descritte. Salvo diversa indicazione, non comprende voli internazionali, assicurazione di viaggio, ingressi non menzionati, bevande, mance e spese personali.</p>"),
 ("4. Modifiche alla prenotazione",f"<p>Se vuoi cambiare date, numero di viaggiatori o itinerario, avvisaci per iscritto il prima possibile a {ML} o su WhatsApp. Faremo sempre il possibile per adattare il viaggio; le modifiche possono incidere sul prezzo in base alla disponibilità.</p>"),
 ("5. Cambiamenti durante il viaggio","<p>Meteo, condizioni delle strade, eventi locali o motivi di sicurezza possono talvolta richiedere di cambiare l’ordine delle visite, il percorso o un alloggio. In questo caso ti proporremo sempre un’alternativa equivalente e ti terremo informato.</p>"),
 ("6. Passaporti, visti e assicurazione","<p>Ogni viaggiatore è responsabile di avere un passaporto valido e, se richiesto per la sua nazionalità, un visto per il Marocco. Consigliamo vivamente un’assicurazione di viaggio che copra spese mediche, rimpatrio e annullamento.</p>"),
 ("7. Salute e attività","<p>Comunicaci prima del viaggio eventuali problemi di salute, mobilità ridotta, gravidanza o esigenze alimentari, così potremo adattare l’itinerario. Durante attività come giri in dromedario, quad, sandboard o trekking, i viaggiatori devono seguire le indicazioni di guide e staff.</p>"),
 ("8. I nostri partner e responsabilità","<p>Selezioniamo con cura hotel, riad, campi, autisti e guide con cui lavoriamo. Non possiamo essere ritenuti responsabili di eventi al di fuori del nostro controllo, come meteo estremo, eventi naturali, scioperi, strade chiuse o ritardi dei voli, ma ti aiuteremo sempre a trovare la soluzione migliore.</p>"),
 ("9. Rispetto e comportamento","<p>Chiediamo a tutti i viaggiatori di rispettare le leggi marocchine, le usanze locali, le persone incontrate e l’ambiente. Possiamo rifiutare di proseguire un servizio in caso di comportamento pericoloso o gravemente irrispettoso.</p>"),
 ("10. Contatti",f"<p>Per qualsiasi domanda su questi termini scrivi a {ML} o contattaci su WhatsApp al {WL}.</p>")]}

FQ={
'en':[("How do I book a tour?","<p>Send us your dates, the number of travellers and the tour you like, through the <a href=\"contact.html\">contact form</a> or on WhatsApp. We reply personally with a detailed itinerary and a quote. Once you are happy with it, a deposit confirms your trip.</p>"),
 ("How much is the deposit, and when do I pay the rest?","<p>The deposit depends on the tour and is written in your quote. The balance is paid on arrival in Morocco.</p>"),
 ("Are your tours private?","<p>Yes. All our tours are private: only you, your family or friends, with your own driver. You never share the vehicle with strangers.</p>"),
 ("Can I change the itinerary?","<p>Of course. Every tour on our website is a suggestion. We can add or remove days, change the starting city, add activities or adapt the pace to your wishes.</p>"),
 ("What is included in the price?","<p>Each tour page shows what is included and not included. In general, the private vehicle with driver, fuel, the accommodation and the meals mentioned are included, while flights, insurance, drinks, tips and personal expenses are not.</p>"),
 ("Can you pick us up at the airport or our hotel?","<p>Yes, the tour can start and end at your hotel, riad or the airport of the departure city. Just send us your flight or hotel details.</p>"),
 ("Which languages do your team speak?","<p>Our team communicates in English, French and Spanish. Tell us your language when you contact us and we will organise the best option for you.</p>"),
 ("What is the best time to visit Morocco and the desert?","<p>Spring and autumn are the most pleasant seasons, but Morocco can be visited all year round with the right rhythm. Read our guide <a href=\"blog-best-time-sahara.html\">The Best Time to Visit the Sahara</a>.</p>"),
 ("What is a night in a desert camp like?","<p>You arrive by camel or 4x4, watch the sunset on the dunes, have dinner, enjoy Berber music by the fire and sleep in a tent. Comfort and luxury camps have real beds and private bathrooms. More in <a href=\"blog-night-desert-camp.html\">A Night in a Sahara Desert Camp</a>.</p>"),
 ("Is Morocco suitable for families and children?","<p>Very much. Children love the camels, the dunes and the gardens, and Moroccans are very kind with them. We adapt the pace and accommodation. See <a href=\"blog-morocco-with-kids.html\">Morocco with Kids</a>.</p>"),
 ("Can you cater for special diets?","<p>Yes. Vegetarian, vegan, gluten-free and other needs can be arranged in most hotels and camps if you tell us in advance.</p>"),
 ("Do I need a visa or travel insurance?","<p>Many nationalities do not need a visa for tourist stays, but the rules depend on your passport, so check with the Moroccan embassy in your country. We strongly recommend travel insurance. See our <a href=\"blog-morocco-practical-tips.html\">practical tips</a>.</p>"),
 ("What should I pack for the desert?","<p>Light clothes for the day, a warm layer for the night, a scarf, sunglasses, sunscreen and comfortable shoes. Our full list: <a href=\"blog-what-to-pack-desert.html\">What to Pack for the Sahara</a>.</p>")],
'es':[("¿Cómo reservo un circuito?","<p>Envíanos tus fechas, el número de viajeros y el circuito que te gusta mediante el <a href=\"contact.html\">formulario de contacto</a> o por WhatsApp. Te respondemos personalmente con un itinerario detallado y un presupuesto. Cuando estés conforme, un depósito confirma tu viaje.</p>"),
 ("¿Cuánto es el depósito y cuándo pago el resto?","<p>El depósito depende del circuito y figura en tu presupuesto. El resto se paga a la llegada a Marruecos.</p>"),
 ("¿Los circuitos son privados?","<p>Sí. Todos nuestros circuitos son privados: solo tú, tu familia o tus amigos, con tu propio conductor. Nunca compartes el vehículo con desconocidos.</p>"),
 ("¿Puedo cambiar el itinerario?","<p>Por supuesto. Cada circuito de la web es una propuesta. Podemos añadir o quitar días, cambiar la ciudad de salida, añadir actividades o adaptar el ritmo a tus deseos.</p>"),
 ("¿Qué incluye el precio?","<p>Cada página de circuito indica lo incluido y lo no incluido. En general se incluyen el vehículo privado con conductor, el combustible, el alojamiento y las comidas mencionadas; no se incluyen vuelos, seguro, bebidas, propinas ni gastos personales.</p>"),
 ("¿Podéis recogernos en el aeropuerto o en el hotel?","<p>Sí, el circuito puede empezar y terminar en tu hotel, riad o en el aeropuerto de la ciudad de salida. Solo envíanos los datos de tu vuelo o alojamiento.</p>"),
 ("¿Qué idiomas habla vuestro equipo?","<p>Nuestro equipo se comunica en inglés, francés y español. Dinos tu idioma al contactarnos y organizaremos la mejor opción para ti.</p>"),
 ("¿Cuál es la mejor época para visitar Marruecos y el desierto?","<p>La primavera y el otoño son las estaciones más agradables, pero Marruecos se puede visitar todo el año con el ritmo adecuado. Lee nuestra guía <a href=\"blog-best-time-sahara.html\">La mejor época para visitar el Sáhara</a>.</p>"),
 ("¿Cómo es una noche en un campamento del desierto?","<p>Llegas en camello o 4x4, ves el atardecer en las dunas, cenas, disfrutas de música bereber junto al fuego y duermes en una jaima. Los campamentos confort y de lujo tienen camas de verdad y baño privado. Más en <a href=\"blog-night-desert-camp.html\">Una noche en un campamento del Sáhara</a>.</p>"),
 ("¿Marruecos es adecuado para familias con niños?","<p>Mucho. A los niños les encantan los camellos, las dunas y los jardines, y los marroquíes son muy cariñosos con ellos. Adaptamos el ritmo y el alojamiento. Mira <a href=\"blog-morocco-with-kids.html\">Marruecos con niños</a>.</p>"),
 ("¿Podéis adaptaros a dietas especiales?","<p>Sí. Las dietas vegetarianas, veganas, sin gluten y otras se pueden organizar en la mayoría de hoteles y campamentos si nos avisas con antelación.</p>"),
 ("¿Necesito visado o seguro de viaje?","<p>Muchas nacionalidades no necesitan visado para estancias turísticas, pero depende de tu pasaporte, así que consulta con la embajada de Marruecos en tu país. Recomendamos encarecidamente un seguro de viaje. Mira nuestros <a href=\"blog-morocco-practical-tips.html\">consejos prácticos</a>.</p>"),
 ("¿Qué llevo para el desierto?","<p>Ropa ligera para el día, una prenda de abrigo para la noche, un pañuelo, gafas de sol, protector solar y calzado cómodo. Nuestra lista completa: <a href=\"blog-what-to-pack-desert.html\">Qué llevar al Sáhara</a>.</p>")],
'fr':[("Comment réserver un circuit ?","<p>Envoyez-nous vos dates, le nombre de voyageurs et le circuit qui vous plaît via le <a href=\"contact.html\">formulaire de contact</a> ou sur WhatsApp. Nous répondons personnellement avec un itinéraire détaillé et un devis. Une fois satisfait, un acompte confirme votre voyage.</p>"),
 ("Quel est le montant de l’acompte et quand payer le solde ?","<p>L’acompte dépend du circuit et figure dans votre devis. Le solde est réglé à votre arrivée au Maroc.</p>"),
 ("Vos circuits sont-ils privés ?","<p>Oui. Tous nos circuits sont privés : vous, votre famille ou vos amis, avec votre propre chauffeur. Vous ne partagez jamais le véhicule avec des inconnus.</p>"),
 ("Puis-je modifier l’itinéraire ?","<p>Bien sûr. Chaque circuit du site est une proposition. Nous pouvons ajouter ou retirer des jours, changer la ville de départ, ajouter des activités ou adapter le rythme à vos envies.</p>"),
 ("Que comprend le prix ?","<p>Chaque page de circuit indique ce qui est inclus et non inclus. En général, le véhicule privé avec chauffeur, le carburant, les hébergements et les repas mentionnés sont inclus ; les vols, l’assurance, les boissons, les pourboires et les dépenses personnelles ne le sont pas.</p>"),
 ("Pouvez-vous venir nous chercher à l’aéroport ou à l’hôtel ?","<p>Oui, le circuit peut commencer et se terminer à votre hôtel, votre riad ou l’aéroport de la ville de départ. Envoyez-nous simplement vos informations de vol ou d’hébergement.</p>"),
 ("Quelles langues parle votre équipe ?","<p>Notre équipe communique en anglais, en français et en espagnol. Indiquez-nous votre langue lors de votre demande et nous organiserons la meilleure option pour vous.</p>"),
 ("Quelle est la meilleure période pour le Maroc et le désert ?","<p>Le printemps et l’automne sont les saisons les plus agréables, mais le Maroc se visite toute l’année avec le bon rythme. Lisez notre guide <a href=\"blog-best-time-sahara.html\">La meilleure période pour visiter le Sahara</a>.</p>"),
 ("Comment se passe une nuit dans un camp du désert ?","<p>Vous arrivez à dos de dromadaire ou en 4x4, admirez le coucher du soleil sur les dunes, dînez, profitez de la musique berbère autour du feu et dormez sous la tente. Les camps confort et de luxe ont de vrais lits et une salle de bain privée. Plus d’infos dans <a href=\"blog-night-desert-camp.html\">Une nuit dans un camp du Sahara</a>.</p>"),
 ("Le Maroc convient-il aux familles avec enfants ?","<p>Tout à fait. Les enfants adorent les dromadaires, les dunes et les jardins, et les Marocains sont très gentils avec eux. Nous adaptons le rythme et l’hébergement. Voir <a href=\"blog-morocco-with-kids.html\">Le Maroc avec des enfants</a>.</p>"),
 ("Pouvez-vous gérer les régimes spéciaux ?","<p>Oui. Les régimes végétarien, vegan, sans gluten et autres peuvent être organisés dans la plupart des hôtels et camps si vous nous prévenez à l’avance.</p>"),
 ("Ai-je besoin d’un visa ou d’une assurance ?","<p>De nombreuses nationalités n’ont pas besoin de visa pour un séjour touristique, mais cela dépend de votre passeport : vérifiez auprès de l’ambassade du Maroc. Nous recommandons vivement une assurance voyage. Voir nos <a href=\"blog-morocco-practical-tips.html\">conseils pratiques</a>.</p>"),
 ("Que mettre dans sa valise pour le désert ?","<p>Des vêtements légers pour la journée, une couche chaude pour la nuit, un foulard, des lunettes de soleil, de la crème solaire et des chaussures confortables. Notre liste complète : <a href=\"blog-what-to-pack-desert.html\">Que mettre dans sa valise pour le Sahara</a>.</p>")],
'it':[("Come prenoto un tour?","<p>Inviaci le tue date, il numero di viaggiatori e il tour che ti piace tramite il <a href=\"contact.html\">modulo di contatto</a> o su WhatsApp. Ti rispondiamo di persona con un itinerario dettagliato e un preventivo. Quando sei soddisfatto, un acconto conferma il viaggio.</p>"),
 ("Quanto è l’acconto e quando pago il resto?","<p>L’acconto dipende dal tour ed è indicato nel preventivo. Il saldo si paga all’arrivo in Marocco.</p>"),
 ("I vostri tour sono privati?","<p>Sì. Tutti i nostri tour sono privati: solo tu, la tua famiglia o i tuoi amici, con il vostro autista. Non condividi mai il veicolo con sconosciuti.</p>"),
 ("Posso modificare l’itinerario?","<p>Certo. Ogni tour del sito è una proposta. Possiamo aggiungere o togliere giorni, cambiare la città di partenza, aggiungere attività o adattare il ritmo ai tuoi desideri.</p>"),
 ("Cosa comprende il prezzo?","<p>Ogni pagina tour indica cosa è incluso e cosa no. In generale sono inclusi il veicolo privato con autista, il carburante, gli alloggi e i pasti menzionati; non sono inclusi voli, assicurazione, bevande, mance e spese personali.</p>"),
 ("Potete venirci a prendere in aeroporto o in hotel?","<p>Sì, il tour può iniziare e finire nel tuo hotel, riad o all’aeroporto della città di partenza. Inviaci semplicemente i dati del volo o dell’alloggio.</p>"),
 ("Quali lingue parla il vostro team?","<p>Il nostro team comunica in inglese, francese e spagnolo. Indicaci la tua lingua quando ci contatti e organizzeremo la soluzione migliore per te.</p>"),
 ("Qual è il periodo migliore per il Marocco e il deserto?","<p>Primavera e autunno sono le stagioni più piacevoli, ma il Marocco si può visitare tutto l’anno con il ritmo giusto. Leggi la nostra guida <a href=\"blog-best-time-sahara.html\">Il periodo migliore per visitare il Sahara</a>.</p>"),
 ("Com’è una notte in un campo nel deserto?","<p>Arrivi in dromedario o in 4x4, guardi il tramonto sulle dune, ceni, ascolti musica berbera intorno al fuoco e dormi in tenda. I campi comfort e di lusso hanno veri letti e bagno privato. Di più in <a href=\"blog-night-desert-camp.html\">Una notte in un campo nel Sahara</a>.</p>"),
 ("Il Marocco è adatto alle famiglie con bambini?","<p>Moltissimo. I bambini adorano i dromedari, le dune e i giardini, e i marocchini sono molto gentili con loro. Adattiamo ritmo e alloggi. Vedi <a href=\"blog-morocco-with-kids.html\">Il Marocco con i bambini</a>.</p>"),
 ("Potete gestire diete particolari?","<p>Sì. Diete vegetariane, vegane, senza glutine e altre si possono organizzare nella maggior parte di hotel e campi se ce lo comunichi prima.</p>"),
 ("Serve un visto o un’assicurazione?","<p>Molte nazionalità non hanno bisogno del visto per soggiorni turistici, ma dipende dal passaporto: verifica con l’ambasciata del Marocco nel tuo paese. Consigliamo vivamente un’assicurazione di viaggio. Vedi i nostri <a href=\"blog-morocco-practical-tips.html\">consigli pratici</a>.</p>"),
 ("Cosa portare nel deserto?","<p>Abiti leggeri per il giorno, uno strato caldo per la notte, un foulard, occhiali da sole, crema solare e scarpe comode. La nostra lista completa: <a href=\"blog-what-to-pack-desert.html\">Cosa portare nel Sahara</a>.</p>")]}

def tdict(l):
    d=dict(BL.UI[l]); d.update(UI[l])
    for nm,src in (('pr',PR),('tm',TM)):
        for i,(h,b) in enumerate(src[l]):
            if h: d[f'lg_{nm}_h{i}']=h
            d[f'lg_{nm}_b{i}']=b
    for i,(q,a) in enumerate(FQ[l]): d[f'lg_fq_q{i}']=q; d[f'lg_fq_a{i}']=a
    return d

BOX='''<aside class="bl-side"><div class="bl-box"><span class="eyebrow" data-i="lg_bx_e">x</span><b data-i="lg_bx_h">x</b><p data-i="lg_bx_p">x</p>
<a class="btn gold" href="contact.html"><span data-i="lg_bx_b">x</span><svg><use href="#i-arrow"/></svg></a>
<a class="btn bl-wa" href="https://wa.me/212659288638" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg><span data-i="lg_bx_w">WhatsApp</span></a></div></aside>'''

def legal_main(nm,img):
    secs=''
    for i,(h,_) in enumerate((PR if nm=='pr' else TM)['en']):
        secs+=(f'<h2 data-i="lg_{nm}_h{i}">x</h2>' if h else '')+f'<div class="bl-sec" data-i="lg_{nm}_b{i}">x</div>'
    return f'''<main id="top">
{BL.hero(img,f'lg_{nm}_h',f'<span data-i="lg_{nm}_c">x</span>','<p class="bl-meta rise d3"><span data-i="lg_upd">x</span></p>')}
<section class="bl-art lg"><div class="in bl-wrap">
  <article class="bl-body reveal">{secs}</article>
  {BOX}
</div></section>
<footer class="foot"></footer>
</main>'''

def faq_main():
    items=''.join(f'<details class="fq-i"{" open" if i==0 else ""}><summary><span data-i="lg_fq_q{i}">x</span><i aria-hidden="true"></i></summary><div class="fq-a" data-i="lg_fq_a{i}">x</div></details>' for i in range(len(FQ['en'])))
    return f'''<main id="top">
{BL.hero('dune-lounge','lg_fq_h','<span data-i="lg_fq_c">x</span>','<p class="lead rise d3" data-i="lg_fq_p">x</p>')}
<section class="bl-art lg"><div class="in bl-wrap">
  <div class="fq reveal">{items}</div>
  {BOX}
</div></section>
{BL.CTA}
<footer class="foot"></footer>
</main>'''

CSS='''
.lg .bl-sec p,.lg .fq-a p{font-size:16.5px}
.lg .bl-body h2{font-size:clamp(22px,2.2vw,30px);margin:38px 0 12px}
.lg .bl-body a,.fq-a a{color:#9a7433;text-decoration:underline;text-underline-offset:3px}
.bl-side .btn.bl-wa{justify-content:center}
.fq{display:grid;gap:14px;max-width:760px}
.fq-i{background:#fff;border:1px solid rgba(22,33,61,.1);border-radius:18px;transition:box-shadow .3s,border-color .3s}
.fq-i[open]{border-color:rgba(201,160,90,.55);box-shadow:0 14px 34px rgba(22,33,61,.08)}
.fq-i summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:18px;padding:20px 24px;font-family:var(--display);font-size:clamp(17px,1.5vw,20px);line-height:1.3;color:#16213d;text-transform:uppercase}
.fq-i summary::-webkit-details-marker{display:none}
.fq-i summary i{flex:none;width:30px;height:30px;border-radius:50%;border:1px solid rgba(201,160,90,.6);position:relative;transition:transform .35s var(--ease),background .3s}
.fq-i summary i::before,.fq-i summary i::after{content:"";position:absolute;left:50%;top:50%;width:11px;height:1.5px;background:#9a7433;transform:translate(-50%,-50%)}
.fq-i summary i::after{transform:translate(-50%,-50%) rotate(90deg);transition:opacity .3s}
.fq-i[open] summary i{background:#16213d;border-color:#16213d;transform:rotate(180deg)}
.fq-i[open] summary i::before{background:var(--gold-hi)}.fq-i[open] summary i::after{opacity:0}
.fq-a{padding:0 24px 22px}.fq-a p{margin:0;font-size:16.5px;line-height:1.8;color:#3c4560}
@media(max-width:640px){.fq-i summary{padding:18px 18px;font-size:16px}.fq-a{padding:0 18px 18px}}
'''
